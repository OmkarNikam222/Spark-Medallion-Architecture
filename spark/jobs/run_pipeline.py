from spark.jobs.run_bronze import main as bronze
from spark.jobs.run_silver import main as silver
from spark.jobs.run_gold import main as gold


def main():

    bronze()

    silver()

    gold()


if __name__ == "__main__":
    main()