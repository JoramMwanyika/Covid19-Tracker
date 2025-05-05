#!/usr/bin/env python3
"""
COVID-19 Global Data Tracker
This script performs comprehensive analysis of COVID-19 data from Our World in Data.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from datetime import datetime
import requests
from pathlib import Path

# Set basic plot style
plt.style.use('default')
sns.set_theme(style='whitegrid')

def download_covid_data():
    """Download the latest COVID-19 data from OWID."""
    url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
    print("Downloading COVID-19 data...")
    response = requests.get(url)
    
    with open('owid-covid-data.csv', 'wb') as f:
        f.write(response.content)
    print("Download complete!")

def load_and_clean_data():
    """Load and perform initial cleaning of the COVID-19 data."""
    # Load the dataset
    df = pd.read_csv('owid-covid-data.csv')
    
    # Convert date to datetime
    df['date'] = pd.to_datetime(df['date'])
    
    # Fill missing values for key columns
    numeric_columns = ['total_cases', 'new_cases', 'total_deaths', 'new_deaths',
                      'total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated']
    
    for col in numeric_columns:
        if col in df.columns:
            df[col] = df[col].fillna(0)
    
    return df

def analyze_global_trends(df):
    """Analyze and plot global COVID-19 trends."""
    # Calculate daily global totals
    global_daily = df.groupby('date')[['new_cases', 'new_deaths']].sum().reset_index()
    
    # Create the plot
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 10))
    
    # Plot new cases
    ax1.plot(global_daily['date'], global_daily['new_cases'], color='blue')
    ax1.set_title('Global Daily New Cases')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Number of Cases')
    
    # Plot new deaths
    ax2.plot(global_daily['date'], global_daily['new_deaths'], color='red')
    ax2.set_title('Global Daily New Deaths')
    ax2.set_xlabel('Date')
    ax2.set_ylabel('Number of Deaths')
    
    plt.tight_layout()
    plt.savefig('global_trends.png')
    plt.close()

def compare_countries(df, countries):
    """Compare COVID-19 metrics across specified countries."""
    # Filter data for selected countries
    country_data = df[df['location'].isin(countries)]
    
    # Create comparison plots
    fig, axes = plt.subplots(2, 1, figsize=(15, 12))
    
    # Total cases by country
    for country in countries:
        country_cases = country_data[country_data['location'] == country]
        axes[0].plot(country_cases['date'], country_cases['total_cases'], label=country)
    
    axes[0].set_title('Total Cases by Country')
    axes[0].set_xlabel('Date')
    axes[0].set_ylabel('Total Cases')
    axes[0].legend()
    
    # Total deaths by country
    for country in countries:
        country_deaths = country_data[country_data['location'] == country]
        axes[1].plot(country_deaths['date'], country_deaths['total_deaths'], label=country)
    
    axes[1].set_title('Total Deaths by Country')
    axes[1].set_xlabel('Date')
    axes[1].set_ylabel('Total Deaths')
    axes[1].legend()
    
    plt.tight_layout()
    plt.savefig('country_comparison.png')
    plt.close()

def analyze_vaccination_progress(df, countries):
    """Analyze vaccination progress for specified countries."""
    # Filter data for selected countries
    country_data = df[df['location'].isin(countries)]
    
    # Create vaccination progress plot
    plt.figure(figsize=(15, 8))
    
    for country in countries:
        country_vax = country_data[country_data['location'] == country]
        plt.plot(country_vax['date'], country_vax['people_fully_vaccinated_per_hundred'],
                label=country)
    
    plt.title('Vaccination Progress by Country')
    plt.xlabel('Date')
    plt.ylabel('Percentage of Population Fully Vaccinated')
    plt.legend()
    plt.grid(True)
    
    plt.savefig('vaccination_progress.png')
    plt.close()

def create_choropleth(df):
    """Create a choropleth map of latest COVID-19 cases."""
    # Get latest data for each country
    latest_data = df.sort_values('date').groupby('location').last().reset_index()
    
    # Create choropleth map
    fig = px.choropleth(latest_data,
                        locations='iso_code',
                        color='total_cases_per_million',
                        hover_name='location',
                        title='Total COVID-19 Cases per Million',
                        color_continuous_scale='Viridis')
    
    fig.write_html('choropleth_map.html')

def main():
    """Main function to run the analysis."""
    # Download and load data
    download_covid_data()
    df = load_and_clean_data()
    
    # Define countries of interest
    countries_of_interest = ['United States', 'India', 'Brazil', 'United Kingdom', 'Kenya']
    
    # Run analyses
    analyze_global_trends(df)
    compare_countries(df, countries_of_interest)
    analyze_vaccination_progress(df, countries_of_interest)
    create_choropleth(df)
    
    print("Analysis complete! Check the output files for visualizations.")

if __name__ == "__main__":
    main()
