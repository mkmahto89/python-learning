from airflow.sdk import dag,task
from datetime import datetime


@dag(
    dag_id="simple_sales_pipeline",
    start_date=datetime(2026,1,1),
    schedule="@daily",
    catchup=False
)
def salespipeline():

    @task
    def extract():
        print("extracting data")

    @task
    def transform():
        print("transform data")        

    @task 
    def load():
        print("loading data")


    #creating task
    extract_task=extract()
    transform_task=transform()
    load_task=load()

            

    extract_task>>transform_task>>load_task


salespipeline()