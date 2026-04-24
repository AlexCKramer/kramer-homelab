ADR 001: Internal Routing and Reverse Proxy (Pi-hole & Traefik)

Date: April 2026

Status: Accepted
Context

Phase 7 of the infrastructure roadmap required establishing an internal routing layer to eliminate the need to memorize IP addresses and port numbers (e.g., 192.168.42.42:8000). This required deploying a local DNS server to handle custom .local domain resolution and a reverse proxy to direct that traffic to the correct Docker containers.

The primary candidates for DNS were Pi-hole and AdGuard Home. The primary candidates for the reverse proxy were Traefik and Nginx Proxy Manager (NPM).
Decision

I elected to deploy Pi-hole for internal DNS and Traefik for the reverse proxy.

    Pi-hole (DNS): Selected for its proven stability, extensive community blocklists, and straightforward local DNS record management.

    Traefik (Reverse Proxy): Selected over NPM to align with Infrastructure-as-Code (IaC) principles. While NPM offers a user-friendly GUI, it requires manual point-and-click configuration for every new service. Traefik integrates natively with the Docker socket, allowing me to define routing rules dynamically via container labels directly inside my docker-compose.yml files.

Consequences

    Positive: Achieved clean, human-readable local routing (e.g., wiki.kramer.local).

    Positive: New services automatically register their own routing rules upon deployment via Docker labels, eliminating manual proxy configuration.

    Positive: Gained network-wide ad and telemetry blocking as a secondary benefit of the DNS layer.

    Negative: Traefik has a significantly steeper initial learning curve for its configuration syntax compared to a GUI-based tool.