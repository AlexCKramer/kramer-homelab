ADR 002: Identity Management and SSO (Authentik & Risk Acceptance)

Date: April 2026

Status: Accepted
Context

Phase 8 required implementing a Single Sign-On (SSO) provider to act as a centralized identity broker for the lab's web dashboards. The goal was to place sensitive infrastructure endpoints behind a unified authentication portal. The main candidates were Authelia and Authentik.

Additionally, I needed to determine the strictness of the access policies, specifically whether to enforce Multi-Factor Authentication (MFA/2FA) for all internal logins.
Decision

I elected to deploy Authentik as the core identity provider and explicitly opted to Accept the Risk of operating without forced 2FA.

    Provider Selection (Authentik): Selected over Authelia due to its robust, enterprise-grade feature set, built-in application outposts, and highly customizable authentication flows.

    Authentication Policy (No 2FA): During the deployment, I successfully configured and tested 2FA implementation. However, I elected to disable it for daily operations. The lab services are not exposed to the public internet; they exist entirely within a local network protected by a UniFi Dream Router handling IDS/IPS.

Consequences

    Positive: Established a single source of truth for identity, allowing me to log into infrastructure dashboards using centralized credentials managed by Bitwarden.

    Positive: Proved technical capability in configuring complex authentication flows and MFA implementation without committing to the operational overhead.

    Positive: Maintained high velocity for daily homelab management by eliminating authentication friction.

    Negative: A compromised device on the internal LAN could theoretically access the dashboards if the attacker also acquired the Bitwarden credentials.

    Mitigation: Network isolation, strict UFW firewall rules on the hosts, and the UniFi gateway perimeter defense mitigate the risk of a local network breach to an acceptable level.