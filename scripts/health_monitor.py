import subprocess
import requests
import time
import redis
import os
from dotenv import load_dotenv

# Load the secrets from the .env file
load_dotenv()

# --- CONFIGURATION ---
# Fetch the webhook securely from the environment
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
ALERT_COOLDOWN_SECONDS = 3600  # 1 hour cooldown per server

# Connect to the Redis Cache on Infra-Services
cache = redis.Redis(host='192.168.42.42', port=6379, decode_responses=True)

SERVERS = {
    "Infra-Services": "192.168.42.42",
    "LinuxGame": "192.168.42.41",
    "Mothership": "192.168.42.5",
    "Holodeck": "192.168.42.8"
}

def ping_server(ip):
    command = ['ping', '-c', '1', '-W', '2', ip]
    result = subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return result == 0

def send_alert(server_name, ip):
    payload = {
        "content": f"🚨 **SRE ALERT:** The server `{server_name}` ({ip}) is completely unresponsive to pings!"
    }
    requests.post(WEBHOOK_URL, json=payload)

# --- MAIN EXECUTION LOOP ---
print("Escape Pod initiating SRE Health Sweep...")

for name, ip in SERVERS.items():
    if ping_server(ip):
        print(f"✅ {name} ({ip}) is ONLINE.")
        # If the server is online, clear any existing alert locks so it can trigger again if it falls
        cache.delete(f"alert:{name}")
    else:
        # Check Redis to see if we already sent an alert recently
        if not cache.exists(f"alert:{name}"):
            print(f"❌ {name} ({ip}) is OFFLINE! Dispatching alert...")
            send_alert(name, ip)
            # Create a lock in Redis that automatically deletes itself after 1 hour (3600 seconds)
            cache.setex(f"alert:{name}", ALERT_COOLDOWN_SECONDS, "alerted")
        else:
            print(f"⚠️ {name} ({ip}) is OFFLINE! (Alert on cooldown, skipping Discord spam)")

print("Sweep complete.")