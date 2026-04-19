# 🎓 Academic Technical Portfolio (2022 - 2025)

This section documents the enterprise-grade labs, architectural designs, and security audits completed during my Bachelor of Applied Science in Information Systems Technology at Santa Fe College.

---

## 🏢 Enterprise Data Center Architecture (Capstone Project)
* **Modular Infrastructure Design:** Architected a scalable, green-energy data center for World Kinect Corporation’s aviation division. Designed the physical footprint utilizing high-density 42U modular racks with integrated chimney structures to enforce strict hot/cold aisle containment.
* **Network Topology:** Specified the internal network architecture using a **Spine-Leaf topology**. Selected **Cisco Nexus 9300** series switches for Top-of-Rack (ToR) deployment and designed the physical layer utilizing Conductive Solid Vinyl Tile (SVT) flooring for static protection.
* **Power & Cooling Efficiency:** Engineered a closed-loop chilled water-cooling system integrated with on-site solar power and battery storage. Incorporated intelligent Power Distribution Units (PDUs) to monitor rack-level energy consumption and optimize Power Usage Effectiveness (PUE).
* **Hazard Mitigation:** Developed disaster recovery protocols targeting **Tier III** reliability standards. Specified FM-200/NOVEC clean agent fire suppression and adaptive HVAC controls (HEPA filtration, positive air pressure) to maintain environmental integrity.

---

## 🖥️ Enterprise Virtualization & High Availability
* **Hypervisor Administration:** Managed Type-1 bare-metal hypervisors, specifically evaluating architectural differences between **VMware vSphere (ESXi)** and **Microsoft Hyper-V**.
* **Infrastructure Reliability:** Executed zero-downtime **vMotion** (Live Migration) of virtual machines and storage payloads across physical hosts.
* **Failover & Automation:** Configured **vSphere High Availability (HA)** for automatic VM failover and evaluated the **Distributed Resource Scheduler (DRS)** for automated load balancing.
* **Lifecycle Management:** Accelerated deployment pipelines by converting configured VMs into reusable templates and deploying systems utilizing the **Open Virtualization Format (OVF)**.
* **Resource Optimization:** Managed resource contention by adjusting **CPU Shares** and utilizing scheduling affinity to prioritize critical workloads across oversubscribed hosts.

---

## ☁️ Public Cloud Ecosystems (AWS & Azure)
* **Serverless Compute:** Developed and deployed HTTP-triggered serverless functions utilizing **Azure Functions** to execute on-demand code.
* **Cloud Storage & Web Hosting:** Provisioned **Azure Web Apps** integrated with **Azure Blob Storage** containers to securely store and serve media assets dynamically.
* **Database as a Service (DBaaS):**
    * **Relational:** Provisioned **Azure SQL Gen5** databases; configured server-level IP firewalls and managed connections via SQL Server Management Studio (SSMS).
    * **NoSQL:** Designed and deployed **Amazon DynamoDB** tables, executing data ingestion and targeted queries utilizing Partition and Sort keys.
* **Cloud Virtualization:** Deployed Ubuntu 24.04 LTS and Windows instances in Azure, configuring **Network Security Groups (NSGs)** to restrict inbound traffic to specific administrative ports (SSH/RDP/1433).

---

## 🗄️ Database Administration & Infrastructure
* **Linux Engine Deployment:** Orchestrated deployments of **PostgreSQL** on **Ubuntu Server**, managing repository configuration, service initialization, and environment tuning.
* **Security Hardening:** Configured `pg_hba.conf` and `postgresql.conf` to enforce **scram-sha-256** authentication and restricted listener addresses to local Unix domain sockets to mitigate unauthorized network access.
* **HA & DR Planning:** Architected a high-availability inventory system with daily encrypted backups (5-week retention) and monthly database imaging for emergency "hot swap" restoration.
* **Data Modeling:** Designed relational schemas with one-to-many/one-to-one relationships, enforcing referential integrity via primary and foreign key constraints.

---

## 📡 Network Engineering & Architecture
* **Campus WLAN Architecture:** Architected a multi-building wireless expansion utilizing **Ubiquiti UISP** Point-to-Point (PtP) bridges and **UniFi Dream Machine Pro Max** gateways to bypass cost-prohibitive fiber runs.
* **Network Simulation (Cisco Packet Tracer):** Designed and troubleshot complex LAN/WLAN topologies. Successfully resolved simulated connectivity failures by identifying and correcting **VLAN mismatches** and misconfigured **MAC Address Whitelisting** policies.
* **Security & Authentication:** Authored enterprise WLAN requirements specifying **WPA3-Enterprise** security, **802.1X** network access control, and EAP-TLS/PEAP protocols.
* **Advanced Subnetting:** Mastered **Variable Length Subnet Masking (VLSM)** and CIDR notation, manually calculating masks from /1 to /32 for optimized addressing efficiency.

---

## 🔎 Network Forensics & Security Operations
* **Packet Analysis (Wireshark):** Performed deep packet inspection of **SSL/TLS handshakes**, TCP/IP headers, and ARP broadcasts to troubleshoot routing behaviors and identify network vulnerabilities.
* **Wireless Pentesting:** Utilized **aircrack-ng** to execute dictionary attacks against WPA2 handshakes and **John the Ripper** for wordlist mangling. Recovered unencrypted FTP credentials captured via packet inspection.
* **Vulnerability Management:** Evaluated enterprise security audit tools, including **Tenable Nessus**, to proactively identify misconfigurations and active attack vectors.
* **Mobile Device Hardening:** Executed hardening protocols on Android systems (Termux), managing system-level updates and auditing memory/process info via `/proc/meminfo`.
* **Wardriving & Auditing:** Performed wireless auditing using **Kismet** to identify hidden SSIDs, rogue access points, and weak WEP encryption.

---

## 🛠️ Software Engineering & DevOps Philosophy
* **Custom Tooling (Python):** Developed a custom ICMP Ping client using the `socket` and `struct` libraries. Managed application timeouts and bitwise checksum calculations for latency measurement.
* **CI/CD & Package Management:** Researched the mechanics of **Continuous Integration/Continuous Delivery** pipelines and the role of Package Management (NuGet, NPM, PyPI) in ensuring version-controlled deployments.
* **Infrastructure-as-Code (IaC) Research:** Evaluated the adoption of **Ansible** for automated network configuration and the transition to **Zero Trust Security** models. *(See this applied in my [Homelab Ansible Baseline](../operations/ansible.md))*
* **Version Control (Git):** Utilized **GitHub** for repository management and branching, documenting commit history for long-term project auditability.

---

## 🚀 Emerging Technologies Research
* **Edge Computing:** Authored technical analyses on how Edge Computing mitigates bandwidth congestion and latency in 5G/IoT deployments by decentralizing processing.
* **AI Infrastructure:** Documented the severe latency and bandwidth constraints of cloud-assisted AI and AR, evaluating cloud-offloading platforms like **Microsoft Azure AR**.