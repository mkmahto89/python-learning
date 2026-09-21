from airflow.sdk import DAG,task
from datetime import datetime
import pandas as pd
sales_asset=Asset("file:///Users/mohitmahto/Documents/Study/sample-file/sales.csv")

@dag(dag_id="dag_produce",
,start_date=datetime(2026,1,1)
,scheduler=None
,catchup=False
)
def produce_dag_pipeline():

    @task(outlets=[sales_asset])
    def produce_file():
        
