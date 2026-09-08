from pyspark.sql import SparkSession
from pyspark.sql.functions import col,floor,rand,pmod,lit
spark=SparkSession.builder.appName("MyAppS").getOrCreate()

Customer=[(1,"C1","Ashok"),(2,"C2","Ram")]
Order=[("O1",1),("O2",1),("O3",2)]
Customer_Col=["CustID","CustCode","CustName"]
Order_Col=["OrderNo","CustID"]

Customer_df=spark.createDataFrame(Customer,Customer_Col)
Order_df=spark.createDataFrame(Order,Order_Col)


Customer_df=Customer_df.withColumn("salt", pmod(hash("CustID"),lit(2)))
 

Customer_df.show()
#Order_df.show()

#Customer_df=Customer_df.withColumn("salt",floor(rand()*2))
#Customer_df.explain("extended")
#Order_df.explain("extended")
#print(spark.sparkContext.defaultParallelism)
#print(Customer_df.rdd.getNumPartitions())
print(spark.conf.get("spark.sql.shuffle.partitions"))

order.groupby("customer_id").count(*).alias("OrderCnt").orderBy(desc("OrderCnt")).show(20)

