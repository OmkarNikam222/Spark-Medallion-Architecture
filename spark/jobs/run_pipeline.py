from spark.common.spark_session import create_spark_session
from spark.common.logger import logger


def main():

    spark = create_spark_session()

    logger.info("=" * 50)
    logger.info("Spark Session Started Successfully")
    logger.info("=" * 50)

    print(f"Spark Version : {spark.version}")

    spark.stop()

    logger.info("Spark Session Closed")


if __name__ == "__main__":
    main()