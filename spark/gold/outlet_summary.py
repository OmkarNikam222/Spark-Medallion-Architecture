from pyspark.sql.functions import sum


def create_outlet_summary(df):

    return (
        df.groupBy(
            "Outlet_Type",
            "Outlet_Size",
            "Outlet_Location_Type"
        )
        .agg(
            sum("Item_Outlet_Sales").alias("Total_Sales")
        )
    )