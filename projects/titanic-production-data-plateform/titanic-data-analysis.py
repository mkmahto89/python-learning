from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import (StructType,StructField,IntegerType,DoubleType,StringType,LongType)
from collections import Counter
 

#Sceanrio 1: Requirement: Load titanic.parquet into a Spark DataFrame.
#printSchema() tells you the structure/data types.
#describe() tells you statistical information about the data.
"""
df=spark.read.parquet("python-learning/projects/titanic-production-data-plateform/titanic.parquet")
df.printSchema()
df.show()
print(df.count())
df.describe().show()

#Scenario 2 — Schema validation

for f in df.schema.fields:
    print(f)
"""

#create spark session 
spark=SparkSession.builder.appName("titanic data analysis").master("local[*]").getOrCreate()

#reading file
df=spark.read.parquet("python-learning/projects/titanic-production-data-plateform/titanic.parquet")

#expected schema
expected_schema=StructType([StructField('PassengerId', LongType(), True),
StructField('Survived', LongType(), True),
StructField('Pclass', LongType(), True),
StructField('Name', StringType(), True),
StructField('Sex', StringType(), True),
StructField('Age', DoubleType(), True),
StructField('SibSp', LongType(), True),
StructField('Parch', LongType(), True),
StructField('Ticket', StringType(), True),
StructField('Fare', DoubleType(), True),
StructField('Cabin', StringType(), True),
StructField('Embarked', StringType(), True)])

#define required columns
required_columns=['PassengerId','Survived','Pclass','Name','Sex']

#schema validation fuction
def validate_dataframe(df,expected_schema,required_columns):
    errors={}

    #1 checking of data is empty 
    if df.isEmpty():
        errors['empty_dataframe']=True
        return errors

    #2 duplicate columns
    duplicates=[
        column
    for column,count in Counter(df.columns).items()
    if count>1
    ]


    if duplicates:
        errors['duplicate_columns']=duplicates


    #3 convert schema into dictionary
    expected={
    field.name:field.dataType
    for field in expected_schema.fields
    }

    #4 convert actual schema into dictionary
    actual={
        field.name:field.dataType
        for field in df.schema.fields
    }

    #5 missing columns
    missing_columns= sorted(set(expected)-set(actual))

    if missing_columns:
        errors["missingcolumns"]=missing_columns

    #6 unexpected columns
    unexpected_columns=set(actual)-set(expected)

    if unexpected_columns:
        error["unexpected_columns"]=unexpected_columns   

    #7 wrong data types
    wrong_types={}

    common_columns=set(expected).intersection(set(actual))

    for col in common_columns:
        if expected[col]!=actual[col]:
            wrong_types[col]={'expected':str(expected[col]),'actual':str(actual[col])}

    if wrong_types:
        error["wrong_data_type"]=wrong_types     

    #8 null values in required columns

    existing_required=set(actual).intersection(set(required_columns))       


    null_result=df.select(
                [F.sum(F.col(c).isNull().cast('int')).alias(c)  
                for c in existing_required]    
    ).first().asDict()  

    null_columns=   {col:cnt
                    for col,cnt in  null_result.items()
                    if cnt>0  
    }  

    if null_columns:
        errors['null_columns']=null_columns

    return errors

errors=validate_dataframe(df,expected_schema,required_columns)

if errors:
    print("schema validation failed")

    for error,detail in errors.items():
        print(error)
        print(detail)

else:
    print("schema validation passed")


spark.stop()






        

 