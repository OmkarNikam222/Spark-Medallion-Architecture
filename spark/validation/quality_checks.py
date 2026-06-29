from pyspark.sql.functions import (
    col,
    count,
    when,
)


def null_report(df):

    return (
        df.select(
            [
                count(
                    when(col(c).isNull(), c)
                ).alias(c)

                for c in df.columns
            ]
        )
    )


def duplicate_count(df):

    return df.count() - df.dropDuplicates().count()


def row_count(df):

    return df.count()


def column_count(df):

    return len(df.columns)