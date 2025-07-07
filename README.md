# 🧬 Data Lineage Tracker

A mock project to simulate an **Amundsen-style** data catalog by extracting DAG metadata from **Airflow**. Visualized lineage and searchable
pipeline components using a custom **Flask** dashboard.

![image](https://github.com/user-attachments/assets/a62d3712-5e85-4e6b-9bf4-2a3f9aa4a14f)

![image](https://github.com/user-attachments/assets/f8ba3764-3fd6-4bd5-8cd3-d6e2e574e8f0)


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

# Activate virtualenv
source venv/bin/activate

# Set Airflow home
export AIRFLOW_HOME=~/lineage-tracker/airflow

# Start Flask (in background)
python3 app.py

# Start Airflow
airflow standalone
