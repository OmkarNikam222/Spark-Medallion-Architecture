from spark.common.helpers import load_config

config = load_config()


def write_silver(df):

    (
        df.write
          .format("delta")
          .mode(config["write_mode"])
          .save(config["paths"]["silver"])
    )