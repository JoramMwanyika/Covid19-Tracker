import nbformat as nbf
import base64
from pathlib import Path

def create_notebook():
    nb = nbf.v4.new_notebook()
    
    # Title and Introduction
    nb['cells'] = [
        nbf.v4.new_markdown_cell("""# COVID-19 Global Data Tracker
        
This notebook analyzes global COVID-19 trends using data from Our World in Data.

## Key Analyses:
1. Global Trends Analysis
2. Country-wise Comparisons
3. Vaccination Progress
4. Geographic Distribution (Choropleth Map)
"""),
        
        # Import Dependencies
        nbf.v4.new_code_cell("""import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from datetime import datetime
import requests

# Set plot style
plt.style.use('default')
sns.set_theme(style='whitegrid')
"""),
        
        # Data Loading Section
        nbf.v4.new_markdown_cell("""## 1. Data Loading and Preprocessing
The data is sourced from Our World in Data's COVID-19 dataset."""),
        
        nbf.v4.new_code_cell("""# Load the preprocessed data
df = pd.read_csv('owid-covid-data.csv')
df['date'] = pd.to_datetime(df['date'])
print(f"Dataset shape: {df.shape}")
df.head()"""),
        
        # Global Trends Section
        nbf.v4.new_markdown_cell("""## 2. Global COVID-19 Trends
Below is the analysis of global trends in cases and deaths."""),
        
        nbf.v4.new_markdown_cell("""### Global Daily Cases and Deaths
![Global Trends](global_trends.png)"""),
        
        # Country Comparisons Section
        nbf.v4.new_markdown_cell("""## 3. Country-wise Comparisons
Comparison of COVID-19 metrics across selected countries."""),
        
        nbf.v4.new_markdown_cell("""### Total Cases and Deaths by Country
![Country Comparison](country_comparison.png)"""),
        
        # Vaccination Progress Section
        nbf.v4.new_markdown_cell("""## 4. Vaccination Progress
Analysis of vaccination progress across countries."""),
        
        nbf.v4.new_markdown_cell("""### Vaccination Progress by Country
![Vaccination Progress](vaccination_progress.png)"""),
        
        # Geographic Distribution Section
        nbf.v4.new_markdown_cell("""## 5. Geographic Distribution
Interactive choropleth map showing the distribution of COVID-19 cases globally.

The interactive map can be found in the `choropleth_map.html` file."""),
        
        # Conclusions Section
        nbf.v4.new_markdown_cell("""## Conclusions

Key findings from our analysis:
1. Global trends show multiple waves of infections
2. Vaccination progress varies significantly by country
3. Case fatality rates differ across regions
4. Economic factors influence testing and reporting capabilities

This analysis provides valuable insights into the global impact and response to the COVID-19 pandemic.""")
    ]
    
    # Save the notebook
    with open('covid19_analysis.ipynb', 'w', encoding='utf-8') as f:
        nbf.write(nb, f)

if __name__ == '__main__':
    create_notebook()
