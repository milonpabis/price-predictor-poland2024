FROM apache/airflow:latest

COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

COPY /opt/airflow/dags /opt/airflow/dags
COPY data_pipeline data_pipeline
COPY db db

