# 🚀 Mothership

## Node Profile
* **Type:** Physical Hardware (Bare-Metal Server)
* **IP Address:** `192.168.42.5`
* **OS:** Proxmox Virtual Environment (VE)
* **SRE Role:** Primary Hypervisor & Infrastructure Backbone

## ⚙️ Operational Compute
* **CPU:** AMD Ryzen 7 2700X (8C/16T) - *Passed through to VMs via `[host]` architecture.*
* **RAM:** 64GB DDR4 (3200MT/s) - *Managed via QEMU Dynamic Ballooning.*
* **GPU:** NVIDIA RTX 2080 - *Currently reserved for host display output. Future expansion for hardware transcoding/AI.*

## 💾 Storage Architecture (5.25 TB Total)
* **Hot Tier (VMs & OS):** 256GB KIOXIA NVMe (`/dev/nvme0n1`)
* **Cold Tier (Bulk & Samba):** ZFS Pool / HDD Array
* **Backups:** VM snapshots managed via Proxmox Backup Server (PBS) using VirtIO guest agent freeze/thaw.

## 🌐 Network Configuration
* **Management UI:** `https://192.168.42.5:8006`
* **Bridge Interface:** `vmbr0`
* **SSH Access:** Key-based authentication (`id_ed25519`) only.

---

## 📊 Asset Register (Hardware Lifecycle)
*Use this table for RMA processing, warranties, and exact replacement matching.*

| Component | Make / Model | Specs | Serial / SKU | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **CPU** | AMD Ryzen 7 2700X | 8C/16T, 3.7GHz Base | [Add Serial] | Socket AM4 |
| **Motherboard** | [Add Make/Model] | [Add Chipset] | [Add Serial] | BIOS Ver: [Add Ver] |
| **RAM Kit 1** | [Add Corsair/G.Skill/etc] | 2x16GB 3200MT/s CL16-18-18-38 | [Add SKU] | Slots A2/B2 |
| **RAM Kit 2** | [Add Corsair/G.Skill/etc] | 2x16GB 3200MT/s CL16-18-18-38 | [Add SKU] | Slots A1/B1 |
| **GPU** | NVIDIA RTX 2080 | 8GB GDDR6 | [Add Serial] | |
| **Boot Drive** | KIOXIA | 256GB NVMe PCIe Gen3 | [Add Serial] | `/dev/nvme0n1` |
| **PSU** | Seasonic FOCUS GX-750 | 750W 80+ Gold | [Add Serial] | Fully Modular |