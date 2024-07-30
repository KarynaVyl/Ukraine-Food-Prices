# Ukraine Food Prices Streamlit App

This Streamlit app provides a visualization of food prices in Ukraine. The application allows users to upload CSV files containing food price data, view and analyze the data, and generate various types of charts.

## Features

- **Data Upload:** Upload CSV files containing food price data.
- **Data Display:** View raw data and summaries in table format.
- **Charts and Graphs:**
  - **Line Charts** showing price trends over time using Plotly.
  - **Bar Charts** for visualizing average prices by date using Matplotlib.
- **Interactive Filters:** Select specific products to filter the displayed data.
- **Progress Indicator:** Shows a loading spinner while processing data.
- **Navigation:** Use a sidebar to navigate between different pages (Home, About Us, Contact).
- **Custom Components:** Includes custom HTML components.

## Data

The app expects CSV files with the following columns:
- `date` - Date of the price record
- `price` - Price of the product
- `category` - Category or name of the product



