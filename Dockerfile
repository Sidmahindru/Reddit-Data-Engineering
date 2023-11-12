FROM apache/airflow:2.7.2-python3.10
COPY requirements.txt /opt/airflow/

USER root
RUN apt-get update && apt-get install -y gcc python3-dev

USER airflow
RUN pip install --user --upgrade pip
RUN pip install --no-cache-dir --user -r /opt/airflow/requirements.txt