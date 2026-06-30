from loguru import logger


def write_silver(df):

    logger.info("Writing Silver Table")

    (
        df.write
        .format("delta")
        .mode("overwrite")
        .saveAsTable("spark_demo.default.silver_bigmart")
    )

    logger.success("Silver Table Created")