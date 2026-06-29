from pyspark.sql.functions import sum


def create_category_summary(df):

    return (
        df.groupBy("Item_Fat_Content")
        .agg(
            sum("Item_Outlet_Sales").alias("Sales")
        )
    )