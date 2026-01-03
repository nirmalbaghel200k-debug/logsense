# LogSense 🔍

LogSense is a full-stack log analysis tool built with FastAPI and a modern web UI.  
It allows users to upload application log files and receive structured, severity-based insights with performance metrics and visualizations.

---

## 🚩 Problem Statement
In real-world systems, raw log files are difficult to analyze quickly. Engineers often need to scan large logs manually to identify critical issues.  
LogSense automates this process by classifying log entries and presenting actionable summaries through a clean web interface.

---

## ✨ Features
- Upload `.log` / `.txt` files via web UI
- Severity classification (Error, Warning, Critical)
- Summary dashboard with counts
- Recurring error detection
- Analysis time measurement (performance awareness)
- Severity distribution chart
- Embedded Swagger API documentation
- Single FastAPI server for frontend + backend

---

## 🧠 System Design
Frontend (HTML + Tailwind + JS)  
→ FastAPI Backend  
→ Log Parser  
→ Severity Engine  
→ JSON Response  
→ UI Visualization

Swagger (OpenAPI) is embedded to demonstrate backend capability.

---

## 🛠 Tech Stack
- Python 3.11
- FastAPI
- HTML, Tailwind CSS
- JavaScript (Fetch API)
- Chart.js
- Swagger / OpenAPI

---

## ▶️ How to Run
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
# LogSense 🔍

LogSense is a full-stack log analysis platform built with FastAPI and a modern web UI.

## Key Features
- Upload and analyze application log files in real time
- Severity classification (Errors, Warnings, Critical)
- Performance-aware analysis with execution time tracking
- Interactive data visualization (Chart.js)
- Embedded Swagger API documentation

## Tech Stack
- Backend: FastAPI (Python)
- Frontend: HTML, Tailwind CSS, Vanilla JavaScript
- Visualization: Chart.js

## Why this project?
Designed to demonstrate backend API design, frontend integration, and system-level thinking in a single deployable service.
