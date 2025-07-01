# 🧬 Data Lineage Tracker

A mock project to simulate metadata-driven lineage using **Flask**, **Airflow**, and **Amundsen**-style frontend.

## 🔧 Tools Used
- Flask
- Airflow (DAG simulation)
- Tailwind CSS + HTML
- Python3.10 on Ubuntu WSL

## ✅ What It Does
- Launches a UI to simulate data lineage flow.
- Runs a mock Airflow DAG that logs metadata events.
- Flask reads those logs and displays timestamps in the UI.

## 📦 Run It Locally

```bash
# Start Flask
python3 app.py

# Start Airflow
airflow standalone
