from loguru import logger


def write_bronze(df):

    logger.info("Writing Bronze Table")

    (
        df.write
        .format("delta")
        .mode("overwrite")
        .saveAsTable("spark_demo.default.bronze_bigmart")
    )

    logger.success("Bronze Table Created")