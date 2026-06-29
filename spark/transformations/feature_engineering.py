from pyspark.sql.functions import year
from pyspark.sql.functions import current_date
from pyspark.sql.functions import col


def create_features(df):

    df = df.withColumn(

        "Outlet_Age",

        year(current_date()) -

        col("Outlet_Establishment_Year")

    )

    return df