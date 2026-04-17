# 🛸 Escape-Pod

## Node Profile
* **Type:** Physical Hardware (Raspberry Pi 4 Model B - 2GB RAM)
* **IP Address:** `192.168.42.6`
* **OS:** Raspberry Pi OS Lite (Headless Debian)
* **Provisioning:** Ansible Baseline Playbook

## SRE Role: Out-of-Band (OOB) Monitor
The `Escape-Pod` operates on the principle of **Fate-Sharing Isolation**. It is deliberately kept physically separate from the `Mothership` hypervisor. 

If Proxmox experiences a catastrophic failure or network bridge collapse, the `Escape-Pod` remains online to detect the outage and dispatch alerts. 

## Active Services
* **Python SRE Health Monitor:** Custom ping-sweep script hooked into Discord Webhooks.
* **Cron Daemon:** Schedules the sweep every 5 minutes and manages log rotation.

## Access & Maintenance
* **SSH:** Key-based authentication only (`id_ed25519`). Password authentication is explicitly disabled via Ansible.
* **Network:** Sits on the standard internal network schema alongside the UniFi/OpenWrt roaming environment.