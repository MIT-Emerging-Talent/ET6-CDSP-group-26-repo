import os
import pandas as pd

"""
This module loads a survey CSV file, cleans and renames columns,
removes empty rows, trims whitespace, and saves the cleaned data
to a specified directory.
"""


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

    # Define scoring scales
    emotional_scale = [
        "I feel a strong emotional reaction (sadness, anger, fear) when I see someone being harmed in a video.",
        "I often feel overwhelmed after watching violent content online.",
        "I feel numb or emotionally detached when watching war-related footage.",
        "I used to react strongly to violent content, but now I rarely feel much.",
        "I avoid watching violent content because it’s emotionally too much for me.",
    ]

    cognitive_scale = [
        "I still think every violent incident deserves attention, no matter how often I see them.",
        "I question why people keep sharing violent videos — it feels unnecessary.",
        "I try to find explanations for what I’m seeing instead of reacting emotionally.",
        "I think the world has always been violent; social media just makes it visible.",
        "I believe violence in the media is just normal now — it doesn’t stand out anymore.",
    ]

    behavioral_scale = [
        "I have taken action (signed a petition, donated, posted) because of something I saw online.",
        "I usually feel compelled to do something after seeing violent content (share, comment, speak up).",
        "I intentionally amplify content about injustice so others see it too.",
        "I scroll past violent content without thinking much about it.",
        "I ignore most violent posts because there's nothing I can do.",
    ]

    # Assign numeric scores based on match index + 1
    df["Emotional Score"] = df[
        "How do you usually feel when you see violent or disturbing content online?"
    ].apply(lambda x: emotional_scale.index(x) + 1 if x in emotional_scale else None)
    df["Cognitive Score"] = df[
        "Which of these thoughts or beliefs sound the most like you?"
    ].apply(lambda x: cognitive_scale.index(x) + 1 if x in cognitive_scale else None)
    df["Behavioral Score"] = df[
        "What do you typically do after seeing violent content online?"
    ].apply(lambda x: behavioral_scale.index(x) + 1 if x in behavioral_scale else None)

    # Define desensitization classifier
    def classify_desensitization(emotional, behavioral):
        if emotional is None or behavioral is None:
            return "Unknown"
        if emotional >= 4:
            return "Desensitized" if behavioral >= 4 else "Numb but Active"
        else:
            return (
                "Empathetic & Active"
                if behavioral <= 2
                else "Emotionally Aware but Passive"
            )

    # Apply classification
    df["Desensitization Type"] = df.apply(
        lambda row: classify_desensitization(
            row["Emotional Score"], row["Behavioral Score"]
        ),
        axis=1,
    )

    # Save the cleaned dataframe to a new CSV file
    output_path = os.path.join(output_dir, "clean_survey_responses.csv")
    df.to_csv(output_path, index=False)

    print(f"Cleaned data saved to {output_path}")
    print(f"Number of responses after cleaning: {len(df)}")
    print(f"Columns after cleaning: {df.columns.tolist()}")


if __name__ == "__main__":
    clean_survey_data(INPUT_PATH, OUTPUT_DIR)
