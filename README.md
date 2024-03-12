# BRFSS Dataset Cleaning and Preparation for Further Analysis
## Project Overview
This project involves cleaning and preparing the Behavioral Risk Factor Surveillance System (BRFSS) dataset for further analysis with nice, colourful graphs. The BRFSS is a United States health survey that looks at behavioral risk factors.

## Dataset
The Dataset used in this comparison is the Anime Dataset in Public Domain, which contains 27 columns. Provided code includes data cleaning, general states comparation by Indicator and later deeper analysis of the state with maxinum percentage value in previous comparation.

Link to the original Dataset:

https://data.world/cdc/behavioral-risk-factor-heart

## Installation
To use the program, follow these steps:

1. Clone the repository: `git clone https://github.com/kefisan/brfss-data-analysis.git`
2. Navigate to the repository directory: `cd brfss-data-analysis`
3. Perform data cleaning: `python3 clean_data.py`
4. Find the state with maximum percentage value in desired Indicator (Prevalence of obesity among US adults by default): `python3 find_states.py`
5. Perform further analysis of the state with maxinum percentage value in previous comparation: `python3 max_state.py`
