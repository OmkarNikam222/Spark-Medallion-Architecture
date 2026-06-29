"""
=========================================================
Spark Medallion Architecture Pipeline
=========================================================

Flow:

Raw CSV
    ↓
Bronze Layer
    ↓
Data Quality Checks
    ↓
Silver Layer
    ↓
Gold Layer (Coming Next)

=========================================================
"""

from spark.common.spark_session import create_spark
from spark.common.logger import logger

# Bronze
from spark.ingestion.read_bigmart import read_bigmart
from spark.ingestion.write_bronze import write_bronze

# Validation
from spark.validation.quality_checks import (
    row_count,
    column_count,
    duplicate_count,
    null_report,
)

# Silver
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
    logger.info("Starting Spark Medallion Pipeline")
    logger.info("=" * 60)

    # -----------------------------------------------------
    # Create Spark Session
    # -----------------------------------------------------

    spark = create_spark()

    logger.info("Spark Session Created Successfully")

    # -----------------------------------------------------
    # Read Raw Dataset
    # -----------------------------------------------------

    logger.info("Reading Raw BigMart Dataset")

    df = read_bigmart(spark)

    logger.info(f"Rows                : {row_count(df)}")
    logger.info(f"Columns             : {column_count(df)}")
    logger.info(f"Duplicate Records   : {duplicate_count(df)}")

    logger.info("Null Value Report")

    null_report(df).show(truncate=False)

    # -----------------------------------------------------
    # Bronze Layer
    # -----------------------------------------------------

    logger.info("=" * 60)
    logger.info("Creating Bronze Layer")
    logger.info("=" * 60)

    write_bronze(df)

    logger.info("Bronze Layer Created Successfully")

    # -----------------------------------------------------
    # Silver Layer
    # -----------------------------------------------------

    logger.info("=" * 60)
    logger.info("Creating Silver Layer")
    logger.info("=" * 60)

    logger.info("Cleaning Missing Values")

    df = clean_missing_values(df)

    logger.info("Standardizing Categorical Values")

    df = standardize_values(df)

    logger.info("Creating Business Features")

    df = create_features(df)

    logger.info("Writing Silver Layer")

    write_silver(df)

    logger.info("Silver Layer Created Successfully")

    # -----------------------------------------------------
    # Pipeline Finished
    # -----------------------------------------------------

    logger.info("=" * 60)
    logger.info("Pipeline Completed Successfully")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()