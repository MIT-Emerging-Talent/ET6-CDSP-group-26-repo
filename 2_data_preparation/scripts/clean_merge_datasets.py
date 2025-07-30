import pandas as pd

# Load raw datasets
gdelt_df = pd.read_csv("../../1_datasets/gdelt_conflict_1_0_RAW.csv")
mm_df = pd.read_csv("../../1_datasets/The Mass Mobilization_RAW.csv")

# Select and clean GDELT
gdelt_clean = gdelt_df[
    [
        "CountryName",
        "Year",
        "SumEvents",
        "GoldsteinScale",
        "EventDescr",
        "EventRootDescr",
    ]
].dropna(subset=["CountryName", "Year"])

gdelt_clean.rename(columns={"CountryName": "country", "Year": "year"}, inplace=True)
gdelt_clean["country"] = gdelt_clean["country"].str.strip().str.lower()
gdelt_clean["year"] = gdelt_clean["year"].astype(int)
gdelt_clean = gdelt_clean.drop_duplicates()

# Group GDELT by country+year
gdelt_grouped = (
    gdelt_clean.groupby(["country", "year"])
    .agg(
        {
            "SumEvents": "sum",
            "GoldsteinScale": "mean",
            "EventDescr": lambda x: "; ".join(x.dropna().astype(str).unique()),
            "EventRootDescr": lambda x: "; ".join(x.dropna().astype(str).unique()),
        }
    )
    .reset_index()
)

# Select and clean MM
mm_clean = mm_df[
    [
        "country",
        "year",
        "protest",
        "participants_category",
        "protesterdemand1",
        "stateresponse1",
    ]
].dropna(subset=["country", "year", "protest", "participants_category"])

mm_clean["country"] = mm_clean["country"].str.strip().str.lower()
mm_clean["year"] = mm_clean["year"].astype(int)
mm_clean = mm_clean.drop_duplicates()

# Group MM claims, demands, responses per country-year
mm_grouped = (
    mm_clean.groupby(["country", "year"])
    .agg(
        {
            "protest": "sum",
            "participants_category": lambda x: x.value_counts().idxmax(),
            "protesterdemand1": lambda x: "; ".join(x.dropna().astype(str).unique()),
            "stateresponse1": lambda x: "; ".join(x.dropna().astype(str).unique()),
        }
    )
    .reset_index()
)

# Merge both grouped datasets
merged_df = pd.merge(gdelt_grouped, mm_grouped, on=["country", "year"], how="inner")

# Export
merged_df.to_csv("../merged_df_with_descriptions.csv", index=False)

print(
    "✅ Done! Dataset saved as merged_df_with_descriptions.csv including topics, demands, and responses."
)
