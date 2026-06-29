from spark.common.spark_session import create_spark
from spark.common.logger import logger

from spark.ingestion.read_bigmart import read_bigmart
from spark.ingestion.write_bronze import write_bronze

from spark.validation.quality_checks import (
    row_count,
    column_count,
    duplicate_count,
    null_report,
)


def main():

    logger.info("=" * 60)
    logger.info("Starting Bronze Pipeline")
    logger.info("=" * 60)

    spark = create_spark()

    df = read_bigmart(spark)

    logger.info(f"Rows : {row_count(df)}")
    logger.info(f"Columns : {column_count(df)}")
    logger.info(f"Duplicates : {duplicate_count(df)}")

    null_report(df).show()

    write_bronze(df)

    logger.info("Bronze Layer Created")


if __name__ == "__main__":
    main()

# Read Raw CSV
#         ↓
# Validation
#         ↓
# Write Bronze