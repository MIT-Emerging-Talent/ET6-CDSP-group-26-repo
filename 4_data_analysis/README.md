# Data Analysis

## 📌 1. Hypothesis

**Hypothesis**:  
Higher exposure to media violence over time is associated with increased protest
activity, rather than emotional desensitization. In particular, we expect that
when violent events are more prominent in the media one year, people are more
likely to mobilize and protest the following year. Additionally, we explore
whether media tone (measured by GoldsteinScale) and past protest activity
influence this relationship.

---

## ⚙️ 2. Modeling Approach

To test this hypothesis, we built a linear regression model (Ordinary Least
Squares, or OLS) to predict **annual protest volume** by country, using:

- `SumEvents`: Annual average count of media-reported violent events  
- `GoldsteinScale`: Annual average tone of those events (lower = more negative)
- `protest_volume`: Total number of protest events in a given year  
- `SumEvents_lag1`: Previous year’s media violence (to account for delayed effects)
- `protest_volume_lag1`: Previous year’s protest volume (to check for habit or momentum)

We chose OLS because it's a well-established, interpretable method for modeling
continuous outcomes like protest volume. By including lagged variables, we aimed
to better capture real-world behavior — people often respond to media coverage
not immediately, but over time. The model estimates how each of these factors
contributes to changes in protest volume year over year.

---

## 📊 3. Key Results

- **R² = 0.82**: This means the model explains approximately 82% of the variation
in protest volume across years — a strong fit.
- **Statistically significant predictor**:  
  - `SumEvents_lag1` had a **positive and statistically significant** effect
(p < 0.05), suggesting that higher media violence in one year leads to more
protests the next year.
- **Non-significant predictors**:  
  - `GoldsteinScale` and `protest_volume_lag1` were **not statistically significant**,
meaning tone and past protest levels didn’t strongly predict current protests in
this model.
- **Coefficient direction**:  
  - `SumEvents_lag1` had a **positive coefficient**, supporting our hypothesis that
people respond to media violence with civic action rather than passivity.

---

## ❗ 4. Constraints and Limitations

Our analysis has several important limitations:

- **Limited sample size**: We modeled roughly 18–20 years of data, which restricts
statistical power.
- **Multicollinearity**: Some predictors (like `SumEvents` and `SumEvents_lag1`)
were correlated, which can make coefficient estimates less stable.
- **Causality caveat**: This is a **correlational model**, not causal. We cannot
say media violence causes protests — only that there’s a predictive relationship.
- **Aggregation**: Our data is **aggregated at the country-year level**, meaning
we ignore variation within countries or between different protest movements.
- **GoldsteinScale nuance**: The tone variable may not fully capture how media
affects public perception — tone can be interpreted differently across contexts
or languages.

---

## 🤔 5. What We Can and Cannot Conclude

**We can confidently say:**

- There is a statistically significant relationship between **media violence in
one year** and **protest activity in the next**.
- This finding **supports the idea of civic mobilization**, not emotional
desensitization, in response to violent news.

**We cannot claim:**

- That media violence directly causes protests.
- That desensitization is ruled out entirely (it may still occur in other
populations or circumstances).
- That these results generalize to all types of protests or all countries.

**Our findings are:**  
**Statistically supported**, but still **exploratory** — useful for generating
insights, not making definitive claims.

---

## ✅ 6. Final Interpretation

Our results support our Hypothesis.  
Rather than becoming emotionally numb, people appear to respond to violent media
coverage with increased protest activity the following year. This suggests that,
in our dataset, media violence is more likely to **fuel civic engagement** than
suppress it — a hopeful sign that awareness still drives action.
