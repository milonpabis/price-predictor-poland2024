from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from data_pipeline.Pipelines import ExtractAndLoad, CleanAndFilter
from db.__init__ import LOCAL_CONNECTION_URI

# MAKE SURE THE DATABASE SERVER IS UP AND RUNNING!!!

DEFAULT_ARGS = {
    "owner": "airflow",
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}

def extract_and_load(**kwargs) -> None:
    ExtractAndLoad(**kwargs).run()

def clean_and_filter(**kwargs) -> None:
    CleanAndFilter(**kwargs).run()

with DAG(
    dag_id="data_pipeline",
    schedule_interval="@daily",
    default_args=DEFAULT_ARGS,
    start_date=datetime(2024, 12, 1),
    catchup=False,
    description="ETL pipeline for real estate (flats) data"
) as dag:
    
    task_data_collection = PythonOperator(
        task_id="data_collection",
        python_callable=extract_and_load,
        op_args=[],
        op_kwargs={"db_uri": LOCAL_CONNECTION_URI}
    )

    task_data_preprocessing = PythonOperator(
        task_id="data_preprocessing",
        python_callable=clean_and_filter,
        op_args=[],
        op_kwargs={"db_uri": LOCAL_CONNECTION_URI}
    )

    task_data_collection >> task_data_preprocessing
