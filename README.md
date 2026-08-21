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

All sales records used in this project are fictional and were created for
demonstration and educational purposes only.

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
├── data/
│   └── sales.csv
├── src/
│   ├── __init__.py
│   └── data_processing.py
├── .gitignore
├── app.py
├── README.md
└── requirements.txt
```

## How It Works

The application follows a simple data processing pipeline:

1. Load the CSV dataset using Pandas.
2. Convert the date column to a datetime format.
3. Calculate revenue from quantity and unit price.
4. Apply the filters selected by the user.
5. Calculate the dashboard metrics.
6. Generate interactive charts using Plotly.
7. Display the results through Streamlit.

Revenue is calculated using:

```text
revenue = quantity × unit_price
```

## Installation

Clone the repository:

```bash
git clone https://github.com/bruno-1405/sales-analytics-dashboard.git
```

Enter the project directory:

```bash
cd sales-analytics-dashboard
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

Streamlit will provide a local URL where the dashboard can be accessed.

## Dataset

The dataset contains the following fields:

| Column | Description |
|---|---|
| `date` | Date of the sale |
| `product` | Product sold |
| `category` | Product category |
| `quantity` | Number of units sold |
| `unit_price` | Price per unit |

Revenue is calculated by the application and is not stored directly in the CSV file.

## Project Goals

This project was created to practice:

- Python programming
- Data manipulation with Pandas
- Data visualization
- Building interactive applications with Streamlit
- Organizing Python code into separate modules
- Using Git and GitHub

## Future Improvements

- [ ] Allow users to upload their own CSV files
- [ ] Add profit and profit margin analysis
- [ ] Add CSV export for filtered data
- [ ] Add automated tests
- [ ] Improve error handling for invalid datasets
- [ ] Add more advanced sales metrics
- [ ] Deploy the application online

## Author

Bruno Covolam Diniz

GitHub: https://github.com/bruno-1405