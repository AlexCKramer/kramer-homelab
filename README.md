# 🚀 Kramer Infrastructure: Homelab Monorepo

Welcome to the central Infrastructure-as-Code (IaC) repository for my personal homelab environment. This repository defines the desired state, deployment automation, and operational documentation for a multi-node bare-metal hypervisor cluster.

## 🏗️ Architecture Overview
This environment is built on **Proxmox VE** and embraces a strict decoupling of the Control Plane from the Compute Nodes. All services are containerized via Docker, orchestrated via Ansible, and meticulously documented.

### Hardware Topology
* **Mothership (Primary Compute):** High-performance host utilizing a hybrid storage architecture (NVMe for OS/VM compute, HDD array for bulk storage). Runs core VMs (`Infra-Services`, `LinuxGame`) and Tier-1 local Samba backups.
* **Holodeck (Disaster Recovery):** Dedicated Proxmox Backup Server (PBS) providing immutable, incremental snapshots and off-node data security.
* **Escape Pod (Utility Node):** Raspberry Pi handling independent, out-of-band network health checks and standalone Python automation.

## 🛠️ Core Technology Stack
* **Virtualization:** Proxmox VE, QEMU/KVM, LXC
* **Containerization:** Docker, Docker Compose
* **Automation & Config Management:** Ansible
* **Storage & Backups:** ZFS, Proxmox Backup Server (PBS), ZSTD Compression
* **Observability:** Grafana, Prometheus, Glances, Watchtower
* **Documentation:** MkDocs (Material Theme)

## 📂 Repository Structure (Monorepo)
This repository centralizes all infrastructure definitions for streamlined version control and deployment:

    kramer-homelab/
    ├── ansible/       # Automated provisioning and baseline security playbooks
    ├── docker/        # Containerized service definitions (YAML) separated by function
    ├── docs/          # MkDocs markdown source files for the infrastructure wiki
    └── scripts/       # Standalone Python automation and out-of-band scripts

## 🛡️ Systems Engineering Principles Applied

### 1. The 3-2-1 Backup Strategy
Data integrity is maintained via a tiered backup architecture:
* **Tier 1 (Rapid Rollback):** Scheduled local `vzdump` archives to internal ZFS/Samba shares for immediate recovery of game servers and application state.
* **Tier 2 (Bare-Metal DR):** Automated, fast-incremental (dirty-bitmap) snapshots pushed to an isolated Proxmox Backup Server (`Holodeck`). 
* **Validation:** Routine "Live-Fire" DR drills are executed to validate data integrity. A recent bare-metal total loss simulation yielded a **Recovery Time Objective (RTO) of < 4 Minutes** with zero data loss.

### 2. Infrastructure as Code (IaC)
Manual configuration is minimized. Service deployments are defined entirely in `docker-compose.yml` files, and bare-metal security baselines are enforced via Ansible playbooks. All secrets are stripped via `.gitignore` and managed locally via `.env` files.

### 3. Observability & Self-Healing
Containers are monitored locally, with updates managed sequentially via Watchtower. Network topology leverages UniFi and OpenWrt for fast-transition roaming and VLAN isolation.

---
*Architected and maintained by [Alex Kramer](https://github.com/AlexCKramer).*