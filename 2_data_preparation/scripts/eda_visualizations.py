import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("2_data_preparation/survey_data/clean_survey_responses.csv")

print(
    df[
        "How do you usually feel when you see violent or disturbing content online?"
    ].value_counts()
)

plt.figure(figsize=(10, 6))
sns.countplot(
    data=df,
    y="How do you usually feel when you see violent or disturbing content online?",
    order=df[
        "How do you usually feel when you see violent or disturbing content online?"
    ]
    .value_counts()
    .index,
    palette="viridis",
)

plt.title("Emotional Response to Violent Content")
plt.xlabel("Number of Responses")
plt.ylabel("Emotion")
plt.tight_layout()
plt.show()
# Calculate the counts and percentages
counts = df[
    "How do you usually feel when you see violent or disturbing content online?"
].value_counts()
percentages = (
    df[
        "How do you usually feel when you see violent or disturbing content online?"
    ].value_counts(normalize=True)
    * 100
)

# Print counts and percentages together
print("Counts and Percentages of Emotional Responses:")
for response, count in counts.items():
    print(f"{response}: {count} responses ({percentages[response]:.1f}%)")
plt.figure(figsize=(8, 8))
plt.pie(
    percentages,
    labels=percentages.index,
    autopct="%1.1f%%",
    colors=sns.color_palette("viridis", len(percentages)),
)
plt.title("Percentage Distribution of Emotional Responses")
plt.show()
import os

# Create directory if it doesn't exist
os.makedirs("1_datasets", exist_ok=True)

# Save bar plot
plt.figure(figsize=(10, 6))
sns.countplot(
    data=df,
    y="How do you usually feel when you see violent or disturbing content online?",
    order=counts.index,
    palette="viridis",
)
plt.title("Emotional Response to Violent Content")
plt.xlabel("Number of Responses")
plt.ylabel("Emotion")
plt.tight_layout()
plt.savefig("1_datasets/emotional_response_barplot.png")
plt.close()

# Save pie chart
plt.figure(figsize=(8, 8))
plt.pie(
    percentages,
    labels=percentages.index,
    autopct="%1.1f%%",
    colors=sns.color_palette("viridis", len(percentages)),
)
plt.title("Percentage Distribution of Emotional Responses")
plt.savefig("1_datasets/emotional_response_piechart.png")
plt.close()

# Save summary as CSV
summary_df = pd.DataFrame(
    {"Response": counts.index, "Count": counts.values, "Percentage": percentages.values}
)
summary_df.to_csv("1_datasets/emotional_response_summary.csv", index=False)
