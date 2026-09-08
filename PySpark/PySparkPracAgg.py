# Initialize Spark session
from pyspark.sql import SparkSession
from pyspark.sql.functions import col,sum
spark = SparkSession.builder.appName('Spark Playground 1').getOrCreate()

#Copy the starter code or load the file path available in the problem statement 
products = spark.createDataFrame([
    (1, "Apple Juice",        "Beverages"),
    (2, "Orange Juice",       "Beverages"),
    (3, "Chocolate Bar",      "Snacks"),
    (4, "Potato Chips",       "Snacks"),
    (5, "Fresh Strawberries", "Fruits"),
    (6, "Sparkling Water",    "Beverages"),
], ["product_id", "name", "category"])

sales = spark.createDataFrame([
    (1, 1, 10, 20),
    (2, 1,  5, 10),
    (3, 2,  8, 16),
    (4, 3,  2,  4),
    (5, 4, 15, 30),
    (6, 4,  5, 10),
    (7, 6, 12, 24),
], ["sale_id", "product_id", "quantity", "revenue"])

inventory = spark.createDataFrame([
    (1, 50, "Warehouse A"),
    (2, 40, "Warehouse A"),
    (2, 20, "Warehouse B"),
    (3, 30, "Warehouse A"),
    (4, 20, "Warehouse A"),
    (4, 15, "Warehouse B"),
    (5, 10, "Warehouse A"),
], ["product_id", "stock", "warehouse"])

# Display the final DataFrame using the display() function.

def getoutput(products,sales,inventory):
  df1=products.join(sales,"product_id","left").groupby("product_id","name","category")\
  .agg(sum("quantity").alias("total_quantity"),sum("revenue").alias("total_revenue"))\
  .select("product_id","name","category","total_quantity","total_revenue")
  df2=products.join(inventory,"product_id","left").groupby("product_id")\
  .agg(sum("stock").alias("total_stock"))\
  .select("product_id","total_stock")
  df=df1.join(df2,"product_id","inner").fillna({"total_quantity":0,"total_revenue":0,"total_stock":0})

  return df
result= getoutput(products,sales,inventory) 
  
  
result.show()
#result.explain("formatted")
#input("Press Enter to stop...")

#inventory.write.mode("overwrite").partitionBy("warehouse").parquet("../study/testpt")
print(inventory.rdd.getNumPartitions())
print(inventory.rdd.glom().collect())



