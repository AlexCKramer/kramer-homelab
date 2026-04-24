# 📔 Incident & Resolution Log

## 2026-04-13: MkDocs Volume & Path Synchronization
**Issue:** Sub-pages (MOTHERSHIP, Incidents) returning 404 errors despite files existing on the host filesystem.
**Root Cause:** A combination of zero-byte (empty) markdown files being ignored by the builder and trailing spaces in the `mkdocs.yml` navigation block.
**Resolution:** 1. Forced content into all `.md` files to ensure they were indexed.
2. Overwrote `mkdocs.yml` using a `cat <<EOF` block to strip all hidden/trailing characters.
3. Performed a hard `down/up` cycle of the Docker container.

## 2026-04-23: Watchtower bootloop
**Issue:** Watchtower container stuck in boot loop.
**Root Cause:** outdated docker image used out of date API that was now blocked.
**Resolution:** Switched image to one still being maintained.
