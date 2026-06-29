from spark.common.spark_session import create_spark
from spark.common.logger import logger

from spark.readers.read_silver import read_silver

from spark.gold.sales_summary import create_sales_summary
from spark.gold.outlet_summary import create_outlet_summary
from spark.gold.item_summary import create_item_summary
from spark.gold.category_summary import create_category_summary
from spark.gold.kpi_summary import create_kpi_summary

from spark.gold.write_gold import write_gold


def main():

    logger.info("=" * 60)
    logger.info("Starting Gold Pipeline")
    logger.info("=" * 60)

    spark = create_spark()

    df = read_silver(spark)

    write_gold(create_sales_summary(df), "sales_summary")
    write_gold(create_outlet_summary(df), "outlet_summary")
    write_gold(create_item_summary(df), "item_summary")
    write_gold(create_category_summary(df), "category_summary")
    write_gold(create_kpi_summary(df), "kpi_summary")

    logger.info("Gold Layer Created")


if __name__ == "__main__":
    main()

# Read Silver
#         ↓
# Sales Summary
# Outlet Summary
# Category Summary
# Item Summary
# KPI Summary
#         ↓
# Write Gold