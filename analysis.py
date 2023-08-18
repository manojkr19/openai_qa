import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency, ttest_ind

# Sample data
data = pd.DataFrame({
    'client_id': [1, 2, 1, 3, 2, 3, 1, 2],
    'sector': ['Tech', 'Health', 'Tech', 'Finance', 'Tech', 'Health', 'Finance', 'Finance'],
    'rating': ['buy', 'sell', 'hold', 'buy', 'buy', 'sell', 'hold', 'buy'],
    'prev_rating': ['hold', 'buy', 'sell', 'hold', 'hold', 'buy', 'sell', 'hold'],
    'price': [150, 120, 130, 140, 155, 118, 135, 142],
    'prev_price': [140, 125, 135, 130, 150, 120, 130, 138],
    'traded': [1, 0, 1, 0, 1, 0, 1, 0]
})

# Correlation Analysis
numeric_features = ['price', 'prev_price']
correlations = data[numeric_features].corrwith(data['traded'])
print("Correlations:\n", correlations)

# Visual Analysis
for feature in ['sector', 'rating', 'prev_rating']:
    plt.figure(figsize=(10, 6))
    sns.countplot(data=data, x=feature, hue='traded')
    plt.title(f"Trade Distribution by {feature}")
    plt.show()

# Chi-Squared Test for Categorical Features
for feature in ['sector', 'rating', 'prev_rating']:
    contingency = pd.crosstab(data[feature], data['traded'])
    chi2, p, _, _ = chi2_contingency(contingency)
    print(f"Chi-Squared Test for {feature}:")
    print(f"Chi2 Value = {chi2}, P-Value = {p}\n")

# T-Test for Continuous Features
for feature in numeric_features:
    group1 = data[data['traded'] == 1][feature]
    group2 = data[data['traded'] == 0][feature]
    t_stat, p_val = ttest_ind(group1, group2)
    print(f"T-Test for {feature}:")
    print(f"T-Statistic = {t_stat}, P-Value = {p_val}\n")
