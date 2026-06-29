from spark.common.helpers import load_config


config = load_config()

RAW_PATH = config["paths"]["raw"]


def read_bigmart(spark):

    df = (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .csv(RAW_PATH)
    )

    return df