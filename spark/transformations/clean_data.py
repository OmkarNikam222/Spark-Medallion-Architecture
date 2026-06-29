from pyspark.sql.functions import col
from pyspark.sql.functions import mean


def clean_missing_values(df):

    # Fill Item_Weight with average
    avg_weight = (
        df.select(mean("Item_Weight"))
          .first()[0]
    )

    df = df.fillna(
        {"Item_Weight": avg_weight}
    )

    # Fill Outlet_Size
    df = df.fillna(
        {"Outlet_Size": "Unknown"}
    )

    return df
    
from pyspark.sql.functions import when


def standardize_values(df):

    df = df.withColumn(

        "Item_Fat_Content",

        when(
            col("Item_Fat_Content").isin(
                "LF",
                "low fat"
            ),
            "Low Fat"

        ).when(

            col("Item_Fat_Content") == "reg",

            "Regular"

        ).otherwise(
            col("Item_Fat_Content")
        )

    )

    return df