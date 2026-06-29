from spark.common.spark_session import create_spark
from spark.common.logger import logger

from spark.readers.read_bronze import read_bronze

from spark.transformations.clean_data import (
    clean_missing_values,
    standardize_values,
)

from spark.transformations.feature_engineering import (
    create_features,
)

from spark.transformations.write_silver import (
    write_silver,
)


def main():

    logger.info("=" * 60)
    logger.info("Starting Silver Pipeline")
    logger.info("=" * 60)

    spark = create_spark()

    df = read_bronze(spark)

    df = clean_missing_values(df)

    df = standardize_values(df)

    df = create_features(df)

    write_silver(df)

    logger.info("Silver Layer Created")


if __name__ == "__main__":
    main()

# Read Bronze
#         ↓
# Clean Data
#         ↓
# Feature Engineering
#         ↓
# Write Silver