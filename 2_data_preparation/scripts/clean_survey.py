import os

import pandas as pd

# Get the absolute path of the current script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Use absolute paths to input/output
INPUT_PATH = os.path.join(
    BASE_DIR, "..", "..", "1_datasets", "violent_content_survey.csv"
)
OUTPUT_DIR = os.path.join(BASE_DIR, "..", "..", "2_data_preparation", "survey_data")


def clean_survey_data(input_path, output_dir):
    # Load CSV
    df = pd.read_csv(input_path)

    # Clean and rename
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

    df.columns = df.columns.str.strip()
    df.rename(
        columns={k: v for k, v in column_renames.items() if k in df.columns},
        inplace=True,
    )
    df.dropna(how="all", inplace=True)

    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].str.strip()

    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "clean_survey_responses.csv")
    df.to_csv(output_path, index=False)

    print(f"✅ Cleaned data saved to {output_path}")
    print(f"🧮 Number of responses: {len(df)}")
    print(f"🧾 Columns: {df.columns.tolist()}")


if __name__ == "__main__":
    clean_survey_data(INPUT_PATH, OUTPUT_DIR)
