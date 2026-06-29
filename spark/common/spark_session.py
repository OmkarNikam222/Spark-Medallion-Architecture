from pyspark.sql import SparkSession


def create_spark_session(app_name: str = "Spark Medallion Architecture") -> SparkSession:
    """
    Create and configure a SparkSession.

    This configuration is suitable for local development.
    It can later be extended for Databricks without changing
    the rest of the project.
    """

    spark = (
        SparkSession.builder
        .appName(app_name)
        .master("local[*]")
        .config("spark.sql.shuffle.partitions", "8")
        .config("spark.driver.memory", "4g")
        .config("spark.executor.memory", "4g")
        .getOrCreate()
    )

    spark.sparkContext.setLogLevel("WARN")

    return spark