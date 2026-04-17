# 📋 SRE Lab Roadmap & Task List

* [x] **Phase 1: The Foundation (Documentation-as-Code)**
    * [x] **Deploy MkDocs-Material via Docker:** Set up the container on `Infra-Services`.
    * [x] **Initialize Git Repository:** Move your notes from Obsidian into the `docs/` folder and perform your first `git commit`.
    * [x] **Create the "Incident Log":** Build a section specifically for documenting hardware failures or configuration errors you've solved.

* [x] **Phase 2: Observability (Monitoring & Metrics)**
    * [x] **Install Node Exporter:** Deploy this to your Proxmox hosts (`MOTHERSHIP` and `HOLODECK`) to pull hardware telemetry.
    * [x] **Deploy Prometheus & Grafana:** Set up the stack in Portainer.
    * [x] **Build the Cluster Dashboard:** Create a single pane of glass showing CPU, RAM, and Network usage for the entire lab.

* [x] **Phase 3: Infrastructure-as-Code (Lifecycle Automation)**
    * [x] **Setup Ansible:** Install Ansible on `Command-Deck` or `Infra-Services`.
    * [x] **Create the "Baseline" Playbook:** Write a script to automate `unattended-upgrades` and security hardening (UFW) across all your Debian/Ubuntu VMs.
    * [x] **Deploy Watchtower:** Automate your Docker container updates with specific "opt-out" labels for critical services.

* [x] **Phase 4: Targeted SRE Skills (Python & NoSQL)**
    * [x] **Write the "Health Check" Python Script:** Build a script that pings your game servers and notifies you (via Discord or email) if they go offline.
    * [x] **Deploy Redis:** Spin up a Redis container to understand how Key-Value stores handle data.
    * [x] **Document the "Glue":** Use MkDocs to explain how your Python script interacts with your services.

* [x] **Phase 5: Reliability Validation (Disaster Recovery)**
    * [x] **Build the "Sacrificial VM":** Create a small test VM on `MOTHERSHIP`.
    * [x] **Live-Fire Restoration:** Back it up to `HOLODECK` via PBS, delete the VM, and time how long it takes to restore it to a fully functional state.
    * [x] **Write the Post-Mortem:** Document the recovery time and any issues encountered in your MkDocs wiki.

* [x] **Phase 6: The Public Portfolio (GitHub)**
    * [x] **Scrub the Git History:** Ensure no sensitive webhooks, IPs, or `.env` files are tracked.
    * [x] **Write the README:** Create a professional `README.md` explaining the architecture and your SRE goals to hiring managers.
    * [x] **Push to Public Repo:** Upload the code to GitHub so it can be linked on your resume.

* [ ] **Phase 7: The Routing Layer (Internal DNS & Reverse Proxy)**
    * [ ] **Deploy Internal DNS:** Spin up Pi-hole or AdGuard Home to handle `.local` domain resolution.
    * [ ] **Deploy Reverse Proxy:** Install Nginx Proxy Manager or Traefik.
    * [ ] **Route the Lab:** Map IPs like `192.168.42.42:8000` to clean URLs like `wiki.kramer.local`.

* [ ] **Phase 8: Identity & Access (Single Sign-On)**
    * [ ] **Deploy SSO Provider:** Spin up Authelia or Authentik.
    * [ ] **Integrate with Proxy:** Lock your web dashboards behind the SSO portal utilizing your Bitwarden credentials and 2FA.