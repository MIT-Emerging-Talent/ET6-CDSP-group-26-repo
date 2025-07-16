import pandas as pd

# Load raw datasets
gdelt_df = pd.read_csv("1_datasets/gdelt_conflict_1_0_RAW.csv")
mm_df = pd.read_csv("1_datasets/The Mass Mobilization_RAW.csv")

# Select relevant columns
gdelt_clean = gdelt_df[["CountryName", "Year", "SumEvents", "GoldsteinScale"]].dropna()
mm_clean = mm_df[["country", "year", "protest", "participants_category"]].dropna()

# Standardize country column names
gdelt_clean.rename(columns={"CountryName": "country", "Year": "year"}, inplace=True)

# Strip + lower country names
gdelt_clean["country"] = gdelt_clean["country"].str.strip().str.lower()
mm_clean["country"] = mm_clean["country"].str.strip().str.lower()

# Convert year to int
gdelt_clean["year"] = gdelt_clean["year"].astype(int)
mm_clean["year"] = mm_clean["year"].astype(int)

# Remove duplicates
gdelt_clean = gdelt_clean.drop_duplicates()
mm_clean = mm_clean.drop_duplicates()

# Merge
merged_df = pd.merge(gdelt_clean, mm_clean, on=["country", "year"], how="inner")

# Export
merged_df.to_csv("2_data_preparation/merged_df.csv", index=False)

print("✅ Done! Cleaned and merged dataset saved as merged_df.csv.")
