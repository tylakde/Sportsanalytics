This repository contains a data analysis project focused on player retention and wagering volume within a sportsbook environment.

The goal of this project was to evaluate the impact of a marketing bonus on player churn and wagering behavior using a simulated dataset of 10,000 players.

    Data: A Python-based simulation (generator.py) creating  player profiles, win/loss ratios, and churn.

    Statistical Modeling: A Jupyter Notebook (analysis.ipynb) performing A/B Testing to difference in wagering behaviour

    Business Intelligence: A Power BI Dashboard providing stakeholders with interactive insights into marketing ROI and player risk.

Based on the analysis of 33.47M in total stakes and a churn rate of 10.62%:

    A/B Test Success: The marketing campaign drove a statistically significant increase in wagering volume for the test group.

    Churn Reduction: Players in the "Test" group exhibited higher retention rates compared to the "Control" group.

    Risk Factors: The GLM identified Win/Loss Ratio as a primary predictor of churn.