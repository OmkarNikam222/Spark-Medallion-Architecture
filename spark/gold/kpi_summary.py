from pyspark.sql.functions import sum, avg, count


def create_kpi_summary(df):

    return df.agg(

        sum("Item_Outlet_Sales").alias("Total_Sales"),

        avg("Item_Outlet_Sales").alias("Average_Sales"),

        avg("Item_MRP").alias("Average_MRP"),

        avg("Item_Visibility").alias("Average_Visibility"),

        count("*").alias("Products")

    )