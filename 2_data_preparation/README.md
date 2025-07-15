# Data Preparation

## Emotional Response Analysis

## 🧹 Data Cleaning & Merging

1. Cleaned raw data from:  
   - `2_data_preparation/mm.csv`  
   - `2_data_preparation/gdelt.csv`  
2. Removed irrelevant columns and handled missing values.  
3. Standardized time formats for consistency.  
4. Merged both datasets based on date to create a unified timeline  
   for analysis.  
5. Exported the final cleaned and merged dataset to:  
   - `1_datasets/clean_merged.csv`  

## 🎯 Objective

Analyze survey responses to understand how participants emotionally react to  
violent or disturbing content they encounter online.

## 🧪 Steps Performed

1. Loaded cleaned survey data from  
   `2_data_preparation/survey_data/clean_survey_responses.csv`.  
2. Calculated response counts and percentages for the emotional reaction  
   question.  
3. Visualized responses using:  
   - A horizontal bar chart  
   - A pie chart showing percentage distribution  

## 📊 Key Findings

- The most common response was **"Anxious"**, making up approximately 30%  
  of total responses.  
- Other frequently mentioned emotions included **"Sad"** and **"Angry"**.  
- A small portion of respondents felt **"Indifferent"**, indicating  
  desensitization.

## 💬 Non-Technical Interpretation

The survey reveals that a majority of participants experience negative  
emotional responses—such as anxiety, sadness, or anger—when exposed to  
violent or disturbing online content. This suggests a high level of emotional  
sensitivity among viewers, which could be shaped by their personal  
experiences or regional context. The relatively low rate of indifference  
implies that even frequent exposure does not necessarily lead to emotional  
numbness in most participants.
