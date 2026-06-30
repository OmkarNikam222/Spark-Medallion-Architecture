from loguru import logger


def write_gold(df, table_name):

    logger.info(f"Writing {table_name}")

    (
        df.write
        .format("delta")
        .mode("overwrite")
        .saveAsTable(f"spark_demo.default.{table_name}")
    )

    logger.success(f"{table_name} created.")