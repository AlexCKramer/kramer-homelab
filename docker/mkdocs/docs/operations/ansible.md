# ⚙️ Ansible Automation

## Architecture Overview
Configuration management and node provisioning are handled via **Ansible**. This ensures that any destroyed or corrupted node can be rebuilt to a secure, production-ready baseline within minutes without manual SSH intervention.

## The Baseline Playbook
The core playbook is designed to take a fresh OS install (like Raspberry Pi OS Lite) and immediately secure it. 

**Standard Baseline Operations:**
1. Update `apt` packages to latest secure versions.
2. Install core utilities (`git`, `docker`, `python3`).
3. Distribute authorized SSH keys across the fleet.
4. Disable password-based SSH logins to harden the perimeter.

## Secrets Management (Ansible Vault)
Sensitive configuration data, particularly `sudo` elevation passwords for the `alex` user across the fleet, are never stored in plaintext playbooks. 

* All privileged escalations are encrypted using **Ansible Vault**.
* The Vault decryption key is stored securely in the local Bitwarden instance (Secure Notes) to prevent Git repository leakage.

## Execution
Playbooks are executed from the main workstation environment targeting specific IP inventories (e.g., `192.168.42.6` for the `Escape-Pod`).