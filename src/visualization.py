import matplotlib.pyplot as plt
import seaborn as sns
import os

OUTPUT_DIR = "outputs/plots"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def overall_trend(df):
    plt.figure(figsize=(10,5))
    sns.lineplot(x='Date', y='Estimated Unemployment Rate (%)', data=df)
    plt.title("Unemployment Rate Trend in India")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/overall_unemployment_trend.png")
    plt.close()

def statewise_covid_unemployment(covid_df):
    plt.figure(figsize=(12,6))
    sns.barplot(
        x='Region',
        y='Estimated Unemployment Rate (%)',
        data=covid_df
    )
    plt.xticks(rotation=90)
    plt.title("State-wise Unemployment During Covid-19")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/statewise_covid_unemployment.png")
    plt.close()

def rural_vs_urban(df):
    plt.figure(figsize=(8,5))
    sns.boxplot(
        x='Area',
        y='Estimated Unemployment Rate (%)',
        data=df
    )
    plt.title("Rural vs Urban Unemployment Rate")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/rural_vs_urban_unemployment.png")
    plt.close()
