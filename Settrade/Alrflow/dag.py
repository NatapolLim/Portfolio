# from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
# from airflow.utils.dates import days_ago
from datetime import datetime

from get_daily_price import concat, get_file

dag = DAG('get_price_dag',
    schedule_interval='0 0 * * *',
    start_date=datetime(2022, 1, 1),
    catchup=False)

get_price = PythonOperator(
    task_id = 'get_daily_price_from_yfinance',
    python_callable=get_file,
    dag=dag
)

concat_data = PythonOperator(
    task_id = 'concat_daily_price_with_main',
    python_callable=concat,
    dag=dag
)

get_price > concat_data