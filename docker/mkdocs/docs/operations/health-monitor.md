# 🚨 SRE Health Monitor (The "Glue")

## Architecture Overview
The SRE Health Monitor is an out-of-band Python script running on the isolated `Escape-Pod` physical node. It sweeps the infrastructure every 5 minutes and pages the private Discord server if a node goes offline. 

To prevent alert fatigue, it utilizes a **Redis Cache** on `Infra-Services` to rate-limit notifications to a 1-hour cooldown per server.

### The "Glue" (How it Works)
1. **Cron (`Escape-Pod`):** Wakes the Python script up every 5 minutes.
2. **Python (`Escape-Pod`):** Pings the target IP (`Mothership`, `Infra-Services`, `LinuxGame`, `Holodeck`). 
3. **Redis (`Infra-Services`):** If a ping fails, Python checks Redis (`192.168.42.42:6379`) for a lock key.
4. **Discord API:** If no lock exists, Python fires the webhook and tells Redis to create a lock with a 3600-second TTL.

## Deployment Instructions

### 1. Prerequisites
* Python 3 with `requests`, `redis`, and `python-dotenv`.
* A running Redis container on `Infra-Services`.
* A valid Discord Webhook.

### 2. Secrets Management (.env)
The Discord Webhook is stored locally on the `Escape-Pod` to keep it out of version control.
**Location:** `~/python_scripts/.env`
```env
DISCORD_WEBHOOK_URL=[https://discord.com/api/webhooks/](https://discord.com/api/webhooks/)...
```

### 3. The Cron Schedule
The script is executed via the `alex` user's crontab on the `Escape-Pod`. Output is piped to a local log file.
```bash
*/5 * * * * /usr/bin/python3 /home/alex/python_scripts/health_monitor.py >> /home/alex/logs/health_monitor.log 2>&1
```

### 4. Viewing Logs
To watch the bot perform its sweep in real-time, tail the log file:
```bash
tail -f ~/logs/health_monitor.log
```