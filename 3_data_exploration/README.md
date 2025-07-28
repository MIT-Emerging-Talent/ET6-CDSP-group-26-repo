# Data Exploration

## 📊 Exploratory Data Analysis: Media Violence, Desensitization & Civic Response

This report documents the data exploration process of our project, which investigates
the psychological and behavioral impacts of exposure to violent media content and
its relationship with civic action, desensitization, and protest trends globally.

---

## 1. 🔍 Overview

Our study combines two main data sources:

- **Survey Dataset**: Self-reported responses from participants about their experiences
with violent content online, emotional/cognitive reactions, and behavioral tendencies.
- **Merged Dataset**: A combination of large-scale event data including the GDELT
Global Knowledge Graph and Mass Mobilization Protest data, merged by country and
year to analyze protest size, frequency, violent events, and government response.

---

## 2. 📋 Survey Data Exploration

### Age Distribution

We begin by understanding the age demographics of our respondents:

![Age Distribution](Visuals/survey_visuals/age_group_distribution.png)

Most participants fall within the 18–24 and 25–35 age groups — making this an analysis
strongly centered around Gen Z and Millennials.

---

### Age vs. Conflict Zone Exposure

![Age vs Conflict Zone](Visuals/survey_visuals/age_group_vs_conflict_zone_experience.png)

Younger respondents (especially 18–24) are more likely to have lived in or near a
conflict zone, possibly due to recent geopolitical crises.

---

### Desensitization Patterns by Age

![Desensitization by Age](Visuals/survey_visuals/desensitization_age.png)

The "Empathetic & Active" type is the most prevalent across all age groups, but
interestingly, “Desensitized” responses slightly increase in older age bands.

---

### Desensitization Distribution

![Desensitization Distribution](Visuals/survey_visuals/distribution_desensitization.png)

Most respondents are **Empathetic & Active**, with a minority falling into the
**Desensitized** or **Numb but Active** categories.

---

### Platform Usage

![Most Used Platforms](Visuals/survey_visuals/most_used_platforms.png)

Instagram is the most used platform, followed by TikTok and YouTube.

---

### Platform vs. Desensitization Type

![Platform Use by Desensitization](Visuals/survey_visuals/Platform_Used_desensitization.png)

Instagram users disproportionately fall into the **Empathetic & Active** category.
Facebook has a more balanced split between types, while Twitter/X and Reddit have
relatively lower engagement.

---

### Type of Violent Content Seen

![Type of Violent Content](Visuals/survey_visuals/type_of_violent_content.png)

**Real-world war footage** is the most frequently encountered violent content,
followed by **graphic news** and **protest crackdowns**. The emotional impact
varies based on content type.

---

### Conflict Zone Exposure vs. Desensitization

![Conflict Zone vs Desensitization](Visuals/survey_visuals/conflict_zone_experience_vs_desensitization.png)

Living near conflict zones does not necessarily lead to desensitization. Respondents
from such areas often remain **empathetically active**, indicating resilience.

---

### Exposure Frequency vs. Desensitization Type

![Exposure Frequency](Visuals/survey_visuals/exposure_frequency.png)

Increased exposure doesn't directly equate to desensitization — even high-frequency
viewers remain emotionally responsive and active.

---

### Behavioral Score by Age

![Behavioral Score by Age](Visuals/survey_visuals/behavioral_score_by_age.png)

There is some variance in behavioral response across age, though no consistent
upward or downward trend.

---

### Emotional vs. Behavioral Score

![Emotional vs Behavioral](Visuals/survey_visuals/emotional_vs_behavioral_score.png)

**Empathetic & Active** respondents show strong correlation between emotional
impact and active response, whereas **Desensitized** individuals show weaker correlation.

---

## 3. 🌍 Merged Dataset Exploration

We now shift focus to protest patterns and violent event trends worldwide using
merged datasets.

---

### 📏 Protest Size Distribution

![Protest Size](Visuals/merged_visuals/protest_size.png)

This chart illustrates the **distribution of protests by participant count**,
revealing how often protests of different sizes occur globally.

- The **most common protest sizes** fall between **100–999** and **50–99 participants**,
suggesting a prevalence of small- to mid-scale mobilizations.
- **Massive protests (>10,000 participants)** are less frequent but still notable.
- The sharp drop beyond the 2,000-participant mark highlights how rare large-scale
protests are.

This distribution helps contextualize the scale of civic participation around
the world.

---

### ⏳ Protest Size Over Time

![Protest Size Over Time](Visuals/merged_visuals/protest_size_over_time.png)

This stacked bar chart shows the number of protests across different size categories
from **1990 to 2019**.

- While **mid-sized protests (100–999 participants)** remain the most common across
all years, there is a **gradual increase in both frequency and diversity of protest
sizes**starting around **2013**.
- Notably, **protests with >10,000 participants** become more frequent after **2014**,
though they still represent a small portion overall.
- The variety of protest sizes appears to **broaden in the post-2010 era**, possibly
reflecting improved reporting, digital mobilization, and heightened global political
tensions.

This visualization supports a **upward trend in protest volume and scale**.

---

### Protest Frequency by Country

![Top Protest Countries](Visuals/merged_visuals/top_10_countries_by_protest_frequency.png)

The data reveals that the **United Kingdom**, **France**, and **Ireland** lead
in protest frequency. This trend likely reflects both an active culture of civic
engagement and reliable documentation practices. Countries with frequent protests
often feature strong traditions of public demonstration tied to political events,
economic grievances, or labor disputes.

However, some countries may be underrepresented due to data limitations or differing
media/reporting infrastructures.

---

### Top 10 Countries by Violent Event Mentions

![Top Violent Events](Visuals/merged_visuals/top_10_most_violent.png)

This chart shows the countries with the most violent events recorded in the GDELT
database. The **United Kingdom**, **India**, and **Russia** are at the top — possibly
because of high media coverage, not just real-world violence. Some countries may
appearhere more due to how much their events are reported, especially in
English-language news.

---

### Top Protest Demands

![Top Protest Demands](Visuals/merged_visuals/top_10_protest_demand.png)

Demands for **political change**, **social justice**, and **accountability** are
most common, reflecting ongoing tensions in governance and inequality.

---

### Top State Responses

![State Responses](Visuals/merged_visuals/top_state_responses.png)

State responses range from **ignore** to **violent crackdowns**, with a significant
number involving the use of force, detention, or legal threats.

---

### Top Types of Violent Events (GDELT CAMEO Codes)

![Violent Event Types](Visuals/merged_visuals/top_violent_events.png)

GDELT event types show dominance in **coercive** and **assault** actions. (See README
appendix for legend on CAMEO categories.)

---

### Violent Events vs Protest Size

![Violent Events vs Protests](Visuals/merged_visuals/violent_events_vs_protests.png)

There is some positive correlation between the intensity of violent events and
protest size, suggesting reactive civic behavior in response to state or media-driven
violence.

---

## 4. 📌 Key Takeaways

- **Most youth are not desensitized**: Even with frequent exposure to violence,
most participants remain emotionally sensitive and socially active.
- **Instagram and YouTube** are the dominant platforms for this demographic and
may shape how violence is consumed.
- **Real-world war footage** remains the most impactful form of content, evoking
strong emotional responses.
- **Protests are increasing globally**, especially in response to state violence
and political crises.
- **Violent events may fuel civic engagement**, contradicting the assumption that
exposure always leads to desensitization.

---

### 📘 Appendix: GDELT CAMEO Violence Categories

The GDELT project uses CAMEO codes to classify types of political events. Below
are the top categories seen in our data:

- **COERCE**: Includes threats, ultimatums, and attempts to force actions through
pressure.
- **FIGHT**: Covers physical conflict, clashes, or armed fighting between groups.
- **ASSAULT**: Direct attacks like bombings, shootings, or military strikes.
- **USE UNCONVENTIONAL MASS VIOLENCE**: Refers to terrorism, suicide bombings,
and mass attacks on civilians.

These categories help us understand the **nature** of violence being reported globally.
