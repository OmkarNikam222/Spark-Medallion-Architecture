from loguru import logger


def write_gold(df, table_name):

    path = f"/Volumes/spark_demo/retail/gold/{table_name}"

    logger.info(f"Writing {table_name}")

    (
        df.write
        .format("delta")
        .mode("overwrite")
        .save(path)
    )

    logger.success(f"{table_name} created.")