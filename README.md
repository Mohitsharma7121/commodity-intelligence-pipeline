# Commodity Intelligence Data Pipeline

## Overview
This project implements an end-to-end data pipeline for commodity price analysis.  
It ingests raw data from multiple sources, cleans and standardizes it, performs feature engineering, and generates actionable signals.

## Pipeline Steps

1. Data Ingestion  
   - Loads data from public sources  
   - Stores raw datasets locally  

2. Data Cleaning & Normalization  
   - Standardizes date and text formats  
   - Adds metadata (region, source)  
   - Merges datasets into a unified schema  

3. Data Validation  
   - Checks for missing values and duplicates  
   - Ensures data consistency  

4. Feature Engineering  
   - Price change (%)  
   - Rolling averages (7, 14, 30)  
   - Volatility  
   - Trend direction  

5. Signal Generation  
   - Demand rising  
   - Price falling  
   - High volatility  
   - Uptrend detection  

## Folder Structure

- scripts/ → pipeline scripts  
- data/raw_data/ → raw datasets  
- data/processed/ → cleaned and feature datasets  
- outputs/ → generated signals  

## Tech Stack
- Python  
- Pandas  

## How to Run

Run scripts in order:

1. python scripts/data_ingestion.py  
2. python scripts/data_cleaning.py  
3. python scripts/data_validation.py  
4. python scripts/feature_engineering.py  
5. python scripts/signal_generation.py  

## Outputs

- cleaned_merged_dataset.csv  
- feature_enriched_dataset.csv  
- signals.csv  

## Pipeline Flow

Raw Data → Cleaning → Validation → Feature Engineering → Signal Generation → Output