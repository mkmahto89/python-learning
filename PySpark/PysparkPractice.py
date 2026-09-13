"""
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark=SparkSession.builder.appName("myApp").getOrCreate()
 

df=spark.parquet,read("titanic.parquet")

df_survived=df.filter(col("Survived")==1).select("name","Sex")
df_NotSurvived=df.filter(col("Survived")==0).select("Name","Sex")

print(df_survived.count())
print(df_NotSurvived.count())

result=( df.groupby("Sex").agg(count("Survived")).alias("Sur_count") )
result.show()

res2=(df.groupby("Sex").agg(count("Survived").alias("sr_cn")).filter(col("sr_cn")>400))
res2.show()
 
data=[
    ("Mohit",20,"cricket,football"),("Raj",21,"hockey,tennis"),("Raju",22,"badminton,rugby")
]

df=spark.createDataFrame(data,["Name","Age","Hobby"])
#df=df.withColumn("Hobby",split("Hobby",","))
#df=df.withColumn("Hobby",explode("Hobby"))

df=df.withColumn("Hobby",split("Hobby",",")).withColumn("Hobby",explode("Hobby"))

df.show()

#df.explain()
#df.explain("extended")
df.explain("formatted")
 
#print(spark.sparkContext.uiWebUrl)

 
 
spark1 = SparkSession.builder \
    .appName("MyApp") \
    .master("local[*]") \
    .config("spark.ui.enabled", "true") \
    .getOrCreate()

df.show()
#input("Press Enter to stop...")

print(spark1.sparkContext.uiWebUrl)
"""
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import (StructType,StructField,IntegerType,DoubleType,LongType,StringType)
from collections import Counter

spark=SparkSession.builder.appName("FileRead").getOrCreate()

df=spark.read.parquet("python-learning/projects/titanic-production-data-plateform/titanic.parquet")
#df.printSchema()

#for f in df.schema.fields:
    #print(f)

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

required_field=['PassengerId','Survived','Pclass','Name','Sex'] 

def validate_input_file(df,expected_schema,required_field):

    errors={}

     #1 checking is dataframe should not be empty
    if df.isEmpty():
        errors['dataframe_empty']='input dataframe is empty'
        return errors


    actual_schema={
        field.name:field.dataType
        for field in df.schema.fields
    }

    expected_schema={
        field.name:field.dataType
        for field in expected_schema.fields
    }

   

    #2 checking if we have any duplicate columns in df
    duplicate_columns=[
    Field
    for Field,Count in Counter(df.schema.fields).items()
    if Count>1
    ]
    if duplicate_columns:
        errors['duplicate_columns']=duplicate_columns

    #3 checking if we have any missing columns
    missing_field=set(expected_schema)-set(actual_schema)

    if missing_field:
        errors['missing_field']=missing_field

    #4 unexpected fields
    unexpected_field=set(actual_schema)-set(expected_schema)

    if unexpected_field:
        errors['unexpected_field']=unexpected_field

    #5 data type mismatch
    common_field=set(expected_schema).intersection(set(actual_schema))
    datatype_mismatch={}
    for col in common_field:
        if expected_schema[col]!=actual_schema[col]:
            datatype_mismatch[col]={'expected':str(expected_schema[col]),'actual':str(actual_schema[col])}
    if datatype_mismatch:            
        errors['datatype_mismatch']=datatype_mismatch

    #6 null value in required field
    nullable_field=df.select([
        F.sum(F.col(cl).isNull().cast('int')).alias(cl)
        for cl in required_field]).first().asDict()

    null_col={ col:cnt 
               for col,cnt in nullable_field.items()
               if cnt>0 }
    if null_col:
        errors['nullable_columns']=null_col    

    return errors           

err=validate_input_file(df,expected_schema,required_field)

if err:
    print('error found')
    for k,v in err.items():
        print(f"{k},{v}")
else:
    print('no error found') 

spark.stop()           







 