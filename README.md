# E--Commerce-data-Cleaning-project-with-python-
A Python-based data preprocessing and cleaning tool that loads raw CSV data, cleans missing or invalid entries, formats fields, and generates summary statistics and visualizations.
The script is ideal for preprocessing 
transactional data before feeding it into analytics or machine learning pipelines.

FEATURES:
- Removal of rows with missing (NaN) values
- Enforcement of valid positive quantities
- Removal of duplicate rows
- Formatting and correction of 'StockCode' to 5-digit numeric values
- Mapping of country names to numeric codes
- Aggregation of customer data by CustomerID (invoices, quantities, pricing)
- Exporting cleaned dataset and customer summary to CSV
- Generation of:
  - Bar chart: Total Quantity by Country
  - Boxplot: Unit Prices
  - Histogram: Quantity distribution

REQUIREMENTS:
- Python 3.x
- pandas
- matplotlib

FILES:
- operation.py              : Main Python script
- Dataset in CSV Format.csv : Input dataset (required for script to run)
- cleaned_data.csv          : Output of cleaned data
- customer_summary.csv      : Aggregated customer summary
- bar_chart_quantity_by_country.png : Bar chart visualization
- boxplot_unit_price.png            : Boxplot of Unit Prices
- histogram_quantity.png            : Histogram of Quantities

USAGE:
1. Place your dataset file named "Dataset in CSV Format.csv" in the same directory as operation.py
2. Run the script:
   python operation.py
3. Check the current directory for output files and charts.

