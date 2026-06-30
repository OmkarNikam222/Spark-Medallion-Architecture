from pyspark.sql import SparkSession


def read_bronze(spark: SparkSession):

    return spark.table("spark_demo.default.bronze_bigmart")