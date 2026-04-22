# SafeGen: Enterprise AI Governance & Observability Stack

SafeGen is a dual-project suite designed to simulate how enterprises safely integrate, govern, and monitor Generative AI applications. It consists of a **Governance API** and a **Real-Time Observability Dashboard**.

## 🏗️ System Architecture
The project follows a decoupled, producer-consumer architecture:
1. **SafeGen API (The Guardrail):** A FastAPI wrapper that intercepts prompts, enforces security policies, and logs telemetry.
2. **SafeGen Dashboard (The Monitor):** A Streamlit application that transforms raw log data into actionable security insights.

---

## 🛡️ Project 1: SafeGen API
Located in `/safegen-api`, this service acts as the security "firewall" between the user and the LLM.

### Key Features
* **Tiered Policy Enforcement:** * **Strict Blocks:** Immediate rejection for high-risk keywords (e.g., `hack`, `bypass`).
    * **Contextual Blocks:** Heuristic checks that allow sensitive words (e.g., `illegal`) if the intent appears informational (ends in `?`).
* **API Key Authentication:** Ensures only authorized internal services can access the gateway.
* **Structured Telemetry:** Logs every request, decision, and violation to a `.jsonl` audit trail for high-concurrency performance.

### Setup & Run
```bash
cd safegen-api
pip install -r requirements.txt
uvicorn main:app --reload# SafeGen: Enterprise AI Governance & Observability Stack

SafeGen is a dual-project suite designed to simulate how enterprises safely integrate, govern, and monitor Generative AI applications. It consists of a **Governance API** and a **Real-Time Observability Dashboard**.

## 🏗️ System Architecture
The project follows a decoupled, producer-consumer architecture:
1. **SafeGen API (The Guardrail):** A FastAPI wrapper that intercepts prompts, enforces security policies, and logs telemetry.
2. **SafeGen Dashboard (The Monitor):** A Streamlit application that transforms raw log data into actionable security insights.

---

## 🛡️ Project 1: SafeGen API
Located in `/safegen-api`, this service acts as the security "firewall" between the user and the LLM.

### Key Features
* **Tiered Policy Enforcement:** * **Strict Blocks:** Immediate rejection for high-risk keywords (e.g., `hack`, `bypass`).
    * **Contextual Blocks:** Heuristic checks that allow sensitive words (e.g., `illegal`) if the intent appears informational (ends in `?`).
* **API Key Authentication:** Ensures only authorized internal services can access the gateway.
* **Structured Telemetry:** Logs every request, decision, and violation to a `.jsonl` audit trail for high-concurrency performance.

### Setup & Run
```bash
cd safegen-api
pip install -r requirements.txt
uvicorn main:app --reload
