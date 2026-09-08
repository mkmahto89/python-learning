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






 