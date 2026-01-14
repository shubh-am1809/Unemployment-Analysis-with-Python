from src.data_loader import load_datasets
from src.analysis import covid_period_data
from src.visualization import (
    overall_trend,
    statewise_covid_unemployment,
    rural_vs_urban
)

def main():
    df_india, df_upto_2020 = load_datasets()

    overall_trend(df_india)

    covid_df = covid_period_data(df_upto_2020)
    statewise_covid_unemployment(covid_df)

    rural_vs_urban(df_india)

    print("All plots saved in outputs/plots/")

if __name__ == "__main__":
    main()
