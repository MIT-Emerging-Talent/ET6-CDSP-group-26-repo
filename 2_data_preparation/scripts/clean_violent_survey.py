"""
This module loads a survey CSV file, cleans and renames columns,
removes empty rows, trims whitespace, and saves the cleaned data
to a specified directory.
"""

import os
import pandas as pd

# Constants (use UPPER_CASE for constants)
INPUT_PATH = r"2_data_preparation\violent_content_survey.csv"
OUTPUT_DIR = "2_data_preparation/survey_data/"


def clean_survey_data(input_path: str, output_dir: str) -> None:
    """Load, clean, and save survey data from CSV."""

    # Load the original survey CSV file
    df = pd.read_csv(input_path)

    # Dictionary to rename columns (update keys with your actual column names in English)
    column_renames = {
        "Timestamp": "timestamp",
        "Age": "age",
        "Conflict Zone Experience": "conflict_zone_experience",
        "Most Used Platform": "platform",
        "Exposure Frequency": "exposure_frequency",
        "Type of Violent Content": "content_type",
        "Emotional Feeling": "emotional_feeling",
        "Beliefs": "belief",
        "Reaction": "reaction",
        "Response Summary": "response_summary",
    }

    # Strip whitespace from column names
    df.columns = df.columns.str.strip()

    # Rename columns using the dictionary (only rename if keys exist)
    df.rename(
        columns={k: v for k, v in column_renames.items() if k in df.columns},
        inplace=True,
    )

    # Remove rows that are completely empty
    df.dropna(how="all", inplace=True)

    # Strip whitespace from string values in all text columns
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].str.strip()

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Save the cleaned dataframe to a new CSV file
    output_path = os.path.join(output_dir, "clean_survey_responses.csv")
    df.to_csv(output_path, index=False)

    print(f"Cleaned data saved to {output_path}")
    print(f"Number of responses after cleaning: {len(df)}")
    print(f"Columns after cleaning: {df.columns.tolist()}")


if __name__ == "__main__":
    clean_survey_data(INPUT_PATH, OUTPUT_DIR)
