# Airbnb Production Dashboard

## Setup

1. Create MySQL DB:
   CREATE DATABASE airbnb_db;

2. Update .env file

3. Run pipeline:
   python data_pipeline_mysql.py

4. Run dashboard:
   streamlit run app.py

## Features
- Data Cleaning
- MySQL Integration
- Interactive Dashboard
- Geo Analysis
- Filters & KPIs

## Docker
docker build -t airbnb-dashboard .
docker run -p 8501:8501 airbnb-dashboard