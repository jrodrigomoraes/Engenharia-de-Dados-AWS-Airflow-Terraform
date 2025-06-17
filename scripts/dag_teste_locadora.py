from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

def imprimir_mensagem():
    print('Dag da locadoura funcionando!!')


default_args = {
    'depends_on_past': False,
    'start_date': datetime(2025, 6, 15),
    'catchup': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=10)
}

dag = DAG(
    dag_id='dag_teste_locadora',
    default_args=default_args,
    description='DAG de teste do projeto Locadora',
    schedule_interval=None)

tarefa_inicial = PythonOperator(
        task_id='imprimir_mensagem',
        python_callable=imprimir_mensagem, dag=dag)

tarefa_inicial