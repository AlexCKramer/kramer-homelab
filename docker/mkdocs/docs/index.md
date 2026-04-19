# 🌐 Kramer Infrastructure & Engineering Wiki

Welcome to the central documentation hub for the Kramer Homelab environment. This wiki serves as the single source of truth for my enterprise-grade infrastructure, disaster recovery runbooks, and professional engineering portfolio.

!!! tip "Hiring Managers & Recruiters"
    If you are reviewing my application, I recommend starting with my **[🎓 Professional Portfolio](portfolio/academic-labs.md)** to see how my academic coursework translates directly into enterprise architectures, DBaaS, and cloud infrastructure.

---

## 🏗️ The Engineering Philosophy
This environment is not just a sandbox; it is treated as a production environment built on **Site Reliability Engineering (SRE)** and **DevOps** principles:

* **Decoupled Architecture:** Compute nodes are strictly separated from disaster recovery and out-of-band edge monitoring.
* **Infrastructure as Code (IaC):** Bare-metal nodes are standardized via Ansible playbooks, and services are orchestrated via Docker Compose.
* **Disaster Recovery:** Redundant networking, tiered ZFS storage, and aggressive Proxmox Backup Server (PBS) snapshots ensure a verified Recovery Time Objective (RTO) of under 4 minutes.
* **Observability:** Centralized telemetry is captured via Prometheus and visualized in Grafana to maintain strict uptime SLAs.

---

## 🗺️ Where to Go Next?

Depending on what you are looking for, here are the best places to start exploring the infrastructure:

* **[Network Topology](network/topology.md):** View the architectural map, VLAN segmentation, and UniFi routing layers.
* **[Operations & Runbooks](operations/ansible.md):** Read through the automated Ansible provisioning scripts and Disaster Recovery procedures.
* **[Incident Management](incidents/log.md):** Review my active Post-Mortem reports detailing how I troubleshoot, mitigate, and resolve hardware and software failures.
* **[SRE Task List](todos/tasks.md):** View my active project roadmap for upcoming infrastructure phases (Single Sign-On, GRC Vulnerability Scanning, App Orchestration).

---
*Architected, documented, and maintained by Alex Kramer.*