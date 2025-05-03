
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Load data
    df = pd.read_csv('/Users/tgalarneau2024/Github stuff/econ_research/data/comtrade.csv')

    # Clean time column and convert to datetime
    df["Time"] = df["Time"].str.extract(r"(\d{4}/\d{1,2})")[0]
    df["Time"] = pd.to_datetime(df["Time"], format="%Y/%m")

    # Normalize country names and convert values to millions
    df["Country"] = df["Country(Area)"]
    df["USD_millions"] = df["Value(USD$ 1000)"] / 1000

    # Filter for key exporters to China
    countries = ["United States", "Japan", "Netherlands"]
    df = df[df["Country"].isin(countries)]

    # Aggregate by month and country
    monthly = df.groupby(["Time", "Country"])["USD_millions"].sum().reset_index()

    # Plot configuration
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=monthly, x="Time", y="USD_millions", hue="Country", marker="o")

    plt.title("Monthly Exports of HS 8542 (Electronic Integrated Circuits)")
    plt.xlabel("Month")
    plt.ylabel("Export Value (USD Millions)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.legend(title="Country")
    plt.grid(True)

    # Save the plot
    plt.savefig("/Users/tgalarneau2024/Github stuff/econ_research/data/comtrade.png", dpi=300)
    plt.show()

if __name__ == "__main__":
    main()
