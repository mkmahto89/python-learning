from pyspark.sql import SparkSession
spark=SparkSession.builder.appName("titanic data analysis").getOrCreate()
df=spark.read.parquet("python-learning/projects/titanic-survival-data-analysis/titanic.parquet")
df.show(5)