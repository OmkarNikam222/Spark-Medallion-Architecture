from spark.common.helpers import load_config


config = load_config()

BRONZE_PATH = config["paths"]["bronze"]


def write_bronze(df):

    (
        df.write
        .format("delta")
        .mode(config["write_mode"])
        .save(BRONZE_PATH)
    )