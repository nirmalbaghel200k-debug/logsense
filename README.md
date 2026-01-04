\# LogSense



LogSense is a FastAPI-based log analysis tool that processes `.log` files and extracts structured insights such as errors, severity, and priority.



\## Features

\- Log file upload and parsing

\- Error \& warning extraction

\- Severity and priority engine

\- Handles empty log files

\- FastAPI REST backend



\## Tech Stack

\- Python 3.11

\- FastAPI

\- Uvicorn



\## Run Locally

```bash

pip install -r requirements.txt

uvicorn app.main:app --reload



