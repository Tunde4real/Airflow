# import internal modules
import datetime as dt
from datetime import timedelta

# import external modules
import pandas as pd
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator


def CSVToJson(**kwargs):
    df = pd.read_csv('/Users/ibrahimaderinto/Desktop/DE/airflow/data/data.csv')
    for i, r in df.iterrows():
        print(r['name'])
    df.to_json('/Users/ibrahimaderinto/Desktop/DE/airflow/data/fromAirflow.json', orient='records')


# def main():
default_args = {
    'owner': 'ibrahim',
    'start_date': dt.datetime(2024, 7, 26),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}


with DAG('MyCSVDAG', default_args = default_args, schedule = timedelta(minutes=5), # '0 * * * *',
    ) as dag:
    print_starting = BashOperator(task_id='starting', bash_command='echo "I am reading the CSV now....."')
    CSVJson = PythonOperator(task_id='convertCSVtoJson', python_callable=CSVToJson)

print_starting >> CSVJson   # Make dag go from bash task to python task
# CSVJson << print_starting         # optional way or use the set_upstream and set_downstream methods
    

''' Some notes
#-- Cron tab --#
Cron tab uses the format -- minute, hour, day of month, month, day of week
a) once
b) hourly  0 * * * *
c) daily  0 0 * * *
d) weekly  0 0 * * 0
e) monthly 0 0 1 * *
f) yearly 0 0 1 1 *
yearly  0 0 1 1 *  means run yearly on January 1 (1 1), at 0:0 
(midnight), on any day of the week (*).
remote_logging = True
remote_base_log_folder = schema://path/to/remote/log
'''