# AIRFLOW COMMANDS

### Start Airflow
```console
airflow webserver
airflow scheduler
``` 
### Start Airflow with one command (less recommended)
```console 
airflow standalone
```
### Run a simple airflow task
```console
airflow tasks test <dag_id> <task_id> [execution_date]
```
