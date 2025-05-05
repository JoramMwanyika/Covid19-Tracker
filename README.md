# COVID-19 Global Data Tracker

## Project Description
A Python-based data analysis project that visualizes and analyzes global COVID-19 trends. This interactive dashboard provides real-time insights into the pandemic's progression, comparing different countries' responses, vaccination efforts, and overall impact using data from Our World in Data.

## Project Objectives

1. **Data Analysis & Visualization**
   - Track and visualize global COVID-19 cases and deaths
   - Monitor vaccination progress across countries
   - Compare pandemic responses between nations
   - Create interactive geographic visualizations

2. **Technical Learning**
   - Practice data cleaning and preprocessing
   - Implement statistical analysis techniques
   - Create effective data visualizations
   - Work with real-world, continuously updated data

## Tools and Libraries

### Core Technologies
- Python 3.8+
- Jupyter Notebook

### Data Analysis
- pandas: Data manipulation and analysis
- numpy: Numerical computations

### Visualization
- matplotlib: Static visualizations
- seaborn: Statistical data visualization
- plotly: Interactive charts and maps

### Data Collection
- requests: Data downloading
- pathlib: File handling

## How to Run the Project

1. **Setup Environment**
   ```bash
   # Install required packages
   pip install -r requirements.txt
   ```

2. **Run Analysis**
   ```bash
   # Option 1: Run Python script
   python covid_analysis.py

   # Option 2: Start Jupyter Notebook
   jupyter notebook
   # Then open covid19_analysis.ipynb
   ```

3. **View Results**
   - Check generated visualizations in project folder:
     - `global_trends.png`: Global case/death trends
     - `country_comparison.png`: Cross-country analysis
     - `vaccination_progress.png`: Vaccination tracking
   - Open `choropleth_map.html` in a web browser for interactive map

## Key Insights

1. **Global Trends**
   - Multiple infection waves identified across regions
   - Varying effectiveness of containment measures

2. **Vaccination Impact**
   - Strong correlation between vaccination rates and case reduction
   - Significant variations in vaccine distribution globally

3. **Regional Patterns**
   - Different response effectiveness across countries
   - Economic factors influencing testing and reporting

4. **Data Limitations**
   - Reporting inconsistencies between countries
   - Testing capacity affecting case numbers
   - Delayed reporting in some regions