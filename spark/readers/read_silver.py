from pyspark.sql import SparkSession


def read_silver(spark: SparkSession):

    return spark.table("spark_demo.default.silver_bigmart")