from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def run_pipeline():
    # Your ETL code here
    pass

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 10, 1),
}

dag = DAG('sales_pipeline', default_args=default_args, schedule_interval='@daily')

run_etl = PythonOperator(
    task_id='run_etl',
    python_callable=run_pipeline,
    dag=dag
)

run_etl