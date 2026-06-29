from pyspark.sql import SparkSession


def create_spark():

    spark = (
        SparkSession.builder
        .appName("Spark Medallion Architecture")
        .getOrCreate()
    )

    return spark