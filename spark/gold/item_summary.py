from pyspark.sql.functions import sum, avg


def create_item_summary(df):

    return (
        df.groupBy("Item_Type")
        .agg(
            sum("Item_Outlet_Sales").alias("Sales"),
            avg("Item_MRP").alias("Average_MRP")
        )
    )