from loguru import logger
from pyspark.sql import SparkSession


def write_gold(df, table_name):

    spark = SparkSession.getActiveSession()

    path = f"/Volumes/spark_demo/retail/gold/{table_name}"

    logger.info(f"Writing {table_name}")

    # --------------------------------------------------
    # Write Delta Files
    # --------------------------------------------------

    (
        df.write
        .format("delta")
        .mode("overwrite")
        .option("overwriteSchema", "true")
        .save(path)
    )

    # --------------------------------------------------
    # Register Unity Catalog Table
    # --------------------------------------------------

    spark.sql(f"""
        CREATE TABLE IF NOT EXISTS spark_demo.default.{table_name}
        USING DELTA
        LOCATION '{path}'
    """)

    logger.success(f"{table_name} created.")