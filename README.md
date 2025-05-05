# COVID-19 Global Data Tracker

An interactive data analysis project that tracks and visualizes global COVID-19 trends using Python. This project provides comprehensive insights into the pandemic's progression, vaccination efforts, and regional impacts.

## Features

- Global COVID-19 case analysis and trend visualization
- Death rates and recovery tracking across countries
- Vaccination progress monitoring with comparative analysis
- Cross-country statistical comparisons
- Interactive choropleth map visualization
- Automated data retrieval and processing
- Comprehensive Jupyter notebook documentation

## Analysis Components

### 1. Global Trends Analysis
- Daily and cumulative case tracking
- Death rate analysis
- Trend visualization using time series plots
- Multiple wave identification and analysis

### 2. Country Comparisons
- Comparative analysis of selected countries
- Case progression visualization
- Death rate comparisons
- Regional impact assessment

### 3. Vaccination Progress
- Vaccination rate tracking
- Population coverage analysis
- Country-wise vaccination comparison
- Progress visualization over time

### 4. Geographic Distribution
- Interactive choropleth map
- Global case distribution
- Regional hotspot identification
- Per-capita analysis

## Setup and Usage

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd Covid19-Tracker
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the analysis:
   - Option 1: Run the complete analysis script
     ```bash
     python covid_analysis.py
     ```
   - Option 2: Open and run the Jupyter notebook
     ```bash
     jupyter notebook covid19_analysis.ipynb
     ```

## Project Structure

- `covid19_analysis.ipynb`: Interactive Jupyter notebook with complete analysis
- `covid_analysis.py`: Python script for automated analysis
- `requirements.txt`: Project dependencies
- Generated visualizations:
  - `global_trends.png`: Worldwide COVID-19 trends
  - `country_comparison.png`: Cross-country analysis
  - `vaccination_progress.png`: Vaccination tracking
  - `choropleth_map.html`: Interactive global distribution map

## Data Source

This project uses the Our World in Data (OWID) COVID-19 dataset, which provides:
- Daily and cumulative cases
- Death counts and rates
- Vaccination data
- Testing information
- Regional metadata

The data is automatically downloaded and processed when running the analysis.

## Tools and Technologies

- Python 3.8+
- Data Analysis: pandas, numpy
- Visualization: matplotlib, seaborn, plotly
- Interactive Environment: Jupyter Notebook
- Data Processing: requests, pathlib

## Results and Insights

The analysis reveals several key insights:
1. Global pandemic waves and their characteristics
2. Vaccination effectiveness and coverage patterns
3. Regional response variations
4. Correlation between various factors (cases, deaths, vaccinations)

## Contributing

Feel free to fork this repository and submit pull requests. You can also:
- Add new analysis components
- Improve visualizations
- Extend country comparisons
- Add new data sources

## License

This project is open-source and available under the MIT License.

## Acknowledgments

- Our World in Data for providing the comprehensive COVID-19 dataset
- Python data science community for the tools and libraries
- Contributors and maintainers of the used packages
- `requirements.txt`: Python dependencies
- `README.md`: Project documentation