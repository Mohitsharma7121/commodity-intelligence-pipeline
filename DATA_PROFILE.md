# DATA PROFILE

## Dataset 1: world_bank.csv
- Source: Public financial dataset (Apple price data)
- Columns: commodity, date, price
- Description: Contains time-series price data for a single commodity
- Missing Values: None
- Duplicates: None
- Data Quality: Clean and structured

## Dataset 2: fao.csv
- Source: Market arrivals dataset (India mandi data)
- Columns: commodity (market names), date, price
- Description: Represents commodity prices across different markets
- Missing Values: None
- Duplicates: None
- Data Quality: Clean but requires normalization

## Observations
- Both datasets follow a similar structure after ingestion
- Date formats were consistent after conversion
- Commodity names required standardization (case, spacing)
- Different sources required additional metadata (region, source)

## Issues Identified
- Inconsistent meaning of "commodity" across datasets
- No region or source information in raw data
- Needed schema alignment before merging

## Actions Taken
- Converted date columns to datetime format
- Standardized commodity names (lowercase, trimmed)
- Added region and source fields
- Unified column structure
- Merged datasets into a single dataset