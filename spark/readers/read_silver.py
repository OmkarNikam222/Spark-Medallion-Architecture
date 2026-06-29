from pyspark.sql import SparkSession


def read_silver(spark: SparkSession):

    return (
        spark.read
        .format("delta")
        .load("/Volumes/spark_demo/retail/silver/bigmart")
    )