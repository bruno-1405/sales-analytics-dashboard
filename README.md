# Sales Analytics Dashboard

Interactive dashboard for exploring and analyzing sales data using Python.

The application processes sales data from a CSV file and provides an interactive
view of revenue, products, categories, and sales trends over time.

## Overview

This project was built as a practical Python project focused on data processing,
analysis, and visualization.

The dashboard allows users to filter the data by category and date range and
view the results through interactive charts and summary metrics.

## Data Disclaimer

All sales data used in this project is **fictional** and was created exclusively
for demonstration and educational purposes.

The dataset does not represent a real company, real transactions, or real
customers. No personal or confidential information is used.

## Features

- Total revenue
- Total quantity sold
- Average ticket
- Revenue over time
- Revenue by category
- Revenue by product
- Filtering by category
- Filtering by date range
- Sales data table

## Technologies

- Python 3
- Pandas
- Streamlit
- Plotly

## Project Structure

```text
sales-analytics-dashboard/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── sales.csv
│
└── src/
    ├── __init__.py
    └── data_processing.py