from pyspark.sql import SparkSession


def read_bronze(spark: SparkSession):

    return (
        spark.read
        .format("delta")
        .load("/Volumes/spark_demo/retail/bronze/bigmart")
    )