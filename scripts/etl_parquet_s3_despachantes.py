from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import boto3
import os
from dotenv import load_dotenv

load_dotenv()

aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')


nome_bucket = 'locadora-analitico-jrm'
raw_prefix = "dimensoes/dim_despachantes/"
prefix_processado = "staging/dim_despachantes/"

s3 = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name='us-east-1'
)


def mover_parquet_s3():
    response = s3.list_objects_v2(Bucket=nome_bucket, Prefix=raw_prefix)
    
    if 'Contents' in response:
        for obj in response['Contents']:
            chave_origem = obj['Key']
            if chave_origem.endswith(".parquet"):
                chave_destino = chave_origem.replace(raw_prefix, prefix_processado)
                print(f'Copiando {chave_origem} para {chave_destino}')
                s3.copy_object(Bucket=nome_bucket, CopySource={'Bucket': nome_bucket, 'Key': chave_origem}, Key=chave_destino)
    else:
        print('Nenhum arquivo encontrado!')
        
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 6, 15),
    'retries': 1,
    'retry_delay': timedelta(seconds=10)
}

dag = DAG(
    dag_id='etl_s3_parquet_despachantes',
    default_args=default_args,
    description='Simulação ETL com parquet no S3',
    schedule_interval=None,
    catchup=False)
    
mover_arquivos = PythonOperator(
    task_id='mover_arquivos_para_staging',
    python_callable=mover_parquet_s3,
    dag=dag)

mover_arquivos