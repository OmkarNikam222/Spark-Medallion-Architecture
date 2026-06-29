from pyspark.sql.functions import sum, avg, count


def create_sales_summary(df):

    return (
        df.groupBy("Outlet_Identifier")
        .agg(
            sum("Item_Outlet_Sales").alias("Total_Sales"),
            avg("Item_Outlet_Sales").alias("Average_Sales"),
            count("*").alias("Products")
        )
    )