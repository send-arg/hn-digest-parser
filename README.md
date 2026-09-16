# ⚡ Hacker News Digest Parser

A zero-dependency Python service that aggregates trending stories and metrics via the official Firebase REST API.

---

### Features
* **Zero External Dependencies:** Implemented using Python's standard `urllib.request` and `json` libraries.
* **Payload Normalization:** Extracts item ID, score, submission title, and target URI.
* **CLI Digest Mode:** Outputs clean, formatted summaries directly to the terminal.

---

### Quick Start

Clone and run directly with standard Python (no `pip install` required):

```bash
python scraper.py
