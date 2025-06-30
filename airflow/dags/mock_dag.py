from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def mock_metadata_push():
    print("🔄 Mock metadata push to Amundsen successful.")
    # This simulates metadata being logged
    with open("/home/darshak/lineage-tracker/logs/metadata_log.txt", "a") as f:
        f.write(f"Metadata pushed at: {datetime.now()}\n")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
}

with DAG(
    dag_id='mock_metadata_lineage_push',
    default_args=default_args,
    schedule='@daily',  # updated for Airflow 2.8+
    catchup=False,
) as dag:
    push_metadata = PythonOperator(
        task_id='push_metadata',
        python_callable=mock_metadata_push,
    )

    push_metadata

