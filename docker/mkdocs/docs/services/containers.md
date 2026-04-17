# 📦 Docker Containers

## Environment Strategy
Containers are orchestrated via `docker-compose.yml` for version control and repeatability. The container infrastructure is intentionally segmented between core services and heavy gaming workloads to prevent resource starvation.

---

## Node: Infra-Services (`192.168.42.42`)
*Resource Allocation: 4GB Max / 2GB Min (QEMU Ballooning), 2 CPU Cores*

This VM acts as the control plane for homelab routing, caching, and dashboards.

| Service | Port | Description |
| :--- | :--- | :--- |
| **Homepage** | `8000` | Unified SRE dashboard. Integrates with Proxmox Backup Server (PBS) and Proxmox VE APIs for widget monitoring. |
| **Portainer** | `9443` | Legacy GUI management for Docker. (Transitioning to pure CLI/Compose). |
| **Watchtower** | N/A | Automated base-image lifecycle management. |
| **Redis** | `6379` | NoSQL in-memory data store. Currently utilized for rate-limiting SRE Discord alerts. Configured with a 60-second RAM-to-disk save state. |

---

## Node: LinuxGame (`192.168.42.41`)
*Resource Allocation: 32GB Max / 16GB Min (QEMU Ballooning), 8 CPU Cores (Host Passthrough)*

Dedicated heavy-compute node for game server hosting. 

| Service | Description | Maintenance Notes |
| :--- | :--- | :--- |
| **Enshrouded** | Voxel action-RPG server. | High CPU/Thread demand. |
| **7 Days to Die** | Survival horde crafting server. | |
| **Palworld** | Creature collection survival. | **Known Issue:** Severe memory leak. Mitigated via daily automated cron restart at `04:00 AM` (`docker restart palworld`). |

*(Future scaling plans include Minecraft and Valheim deployments).*