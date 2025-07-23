import pandas as pd
import matplotlib.pyplot as plt

# Load your data
df = pd.read_csv("Dataset in CSV Format.csv")

# Step 1: Remove rows with NaN
df = df.dropna(axis=0)
print("Cleaned DataFrame shape:", df.shape)
print("Number of NaN values after cleaning:", df.isnull().sum().sum())

# Step 2: Ensure 'Quantity' is greater than 0
if 'Quantity' in df.columns:
    df["Quantity"] = df["Quantity"].apply(lambda x: max(x, 1))
print("In Quantity Column all the Negative or NUll values replaced and now is greater than 1 ")    

# Step 3: Drop duplicate rows
df.drop_duplicates(inplace=True)
print("Number of duplicates after cleaning:", df.duplicated().sum())

# Step 4: Correct 'StockCode' format
if 'StockCode' in df.columns:
    # Ensure 'StockCode' is treated as a string first
    df["StockCode"] = df["StockCode"].astype(str)
    
    # Remove non-numeric characters
    df["StockCode"] = df["StockCode"].str.extract(r'(\d+)')
    
    # Fill missing values with '00000' and ensure all codes are 5-digit integers
    df["StockCode"] = df["StockCode"].fillna("12345").astype(int).astype(str).str.zfill(5)
    print("StockCode column formatted successfully as 5-digit integers.")

# Step 5: Map countries to numeric codes
if 'Country' in df.columns:
    country_mapping = {
        "Australia": 1, "EIRE": 2, "France": 3,
        "Germany": 4, "Netherlands": 5,
        "Norway": 6, "United Kingdom": 7
    }
    # Replace country names with numbers
    df["Country"] = df["Country"].map(country_mapping)
    print("All the country names replaced with the numeric characters.")

# Step 6: Group by CustomerID and aggregate necessary columns
if 'CustomerID' in df.columns and 'InvoiceNo' in df.columns:
    summary = df.groupby('CustomerID').agg({
        'InvoiceNo': 'nunique',  # Number of unique invoices
        'Quantity': 'sum',       # Total quantity purchased
        'UnitPrice': 'mean',     # Average unit price
        'Country': 'first',      # Retain the country (if consistent per customer)
        'InvoiceDate': 'first'  
    }).reset_index()
    
    # Save the summary to a new CSV file
    summary.to_csv("customer_summary.csv", index=False)
    print("Customer summary saved to customer_summary.csv")

# Visualization Section
# Step 7: Generate Bar Chart for Total Quantity by Country
if 'Country' in df.columns and 'Quantity' in df.columns:
    country_quantity = df.groupby('Country')['Quantity'].sum()
    plt.figure(figsize=(10, 6))
    country_quantity.plot(kind='bar', color='skyblue')
    plt.title("Total Quantity Sold by Country")
    plt.xlabel("Country")
    plt.ylabel("Total Quantity")
    plt.xticks(rotation=45)
    plt.savefig("bar_chart_quantity_by_country.png")
    plt.show()
print("Bar Chart for Total Quantity by Country")

# Step 8: Generate Boxplot for UnitPrice
if 'UnitPrice' in df.columns:
    plt.figure(figsize=(8, 5))
    plt.boxplot(df['UnitPrice'], vert=False, patch_artist=True, boxprops=dict(facecolor="lightblue"))
    plt.title("Boxplot of Unit Prices")
    plt.xlabel("Unit Price")
    plt.savefig("boxplot_unit_price.png")
    plt.show()
print("Boxplot for UnitPrice")

# Step 9: Generate Histogram for Quantity
if 'Quantity' in df.columns:
    plt.figure(figsize=(8, 5))
    plt.hist(df['Quantity'], bins=20, color='lightgreen', edgecolor='black')
    plt.title("Histogram of Quantities")
    plt.xlabel("Quantity")
    plt.ylabel("Frequency")
    plt.savefig("histogram_quantity.png")
    plt.show()
print("Histogram for Quantity Column")

# Save the cleaned and updated data
df.to_csv("cleaned_data.csv", index=False)
print("Cleaned and updated data saved to cleaned_data.csv")