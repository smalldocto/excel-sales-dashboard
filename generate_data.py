import pandas as pd
import numpy as np

# Make results reproducible
np.random.seed(42)

# Number of transactions
n = 1000

# Product information
products = {
    "Laptop": ("Electronics", 850, 600),
    "Monitor": ("Electronics", 420, 280),
    "Headphones": ("Electronics", 120, 60),
    "Keyboard": ("Electronics", 75, 40),
    "Office Chair": ("Furniture", 275, 170),
    "Desk": ("Furniture", 325, 200),
    "Printer": ("Electronics", 240, 150),
    "Bookshelf": ("Furniture", 190, 110)
}

# Countries and regions
countries = {
    "USA": "North America",
    "Canada": "North America",
    "UK": "Europe",
    "Germany": "Europe",
    "Nigeria": "Africa",
    "Kenya": "Africa",
    "Australia": "Oceania",
    "India": "Asia"
}

# Customer names
first_names = [
    "Alex", "Jordan", "Taylor", "Morgan", "Casey",
    "Jamie", "Avery", "Riley", "Cameron", "Drew",
    "Sam", "Chris", "Mia", "Noah", "Emma",
    "Liam", "Olivia", "Ethan", "Sophia", "Daniel"
]

last_names = [
    "Smith", "Johnson", "Brown", "Davis", "Wilson",
    "Taylor", "Anderson", "Thomas", "Moore", "Martin",
    "Clark", "Lewis", "Walker", "Hall", "Young"
]

# Random dates across 2025
dates = pd.date_range(
    "2025-01-01",
    "2025-12-31"
)

# Store generated records
rows = []

# Generate transactions
for i in range(n):

    # Random selections
    order_date = np.random.choice(dates)

    country = np.random.choice(
        list(countries.keys())
    )

    product = np.random.choice(
        list(products.keys())
    )

    category, base_price, unit_cost = products[product]

    # Quantity purchased
    quantity = np.random.choice(
        [1, 2, 3, 4, 5, 6],
        p=[0.28, 0.27, 0.20, 0.13, 0.07, 0.05]
    )

    # Discount applied
    discount = np.random.choice(
        [0, 0.05, 0.10, 0.15, 0.20],
        p=[0.45, 0.25, 0.18, 0.09, 0.03]
    )

    # Slight variation in product price
    unit_price = round(
        base_price * np.random.uniform(0.95, 1.08),
        2
    )

    # Calculate sales
    sales = round(
        quantity * unit_price * (1 - discount),
        2
    )

    # Calculate cost
    cost = round(
        quantity * unit_cost,
        2
    )

    # Calculate profit
    profit = round(
        sales - cost,
        2
    )

    # Generate customer name
    first_name = np.random.choice(first_names)
    last_name = np.random.choice(last_names)

    customer = f"{first_name} {last_name}"

    # Payment method
    payment_method = np.random.choice(
        [
            "Credit Card",
            "Debit Card",
            "Bank Transfer",
            "PayPal"
        ],
        p=[0.38, 0.25, 0.20, 0.17]
    )

    # Sales channel
    sales_channel = np.random.choice(
        [
            "Online",
            "Retail Store",
            "Marketplace"
        ],
        p=[0.55, 0.25, 0.20]
    )

    # Add transaction to list
    rows.append([
        f"ORD-{100001 + i}",
        pd.Timestamp(order_date).date(),
        customer,
        country,
        countries[country],
        product,
        category,
        quantity,
        unit_price,
        discount,
        sales,
        cost,
        profit,
        payment_method,
        sales_channel
    ])


# Create DataFrame
df = pd.DataFrame(
    rows,
    columns=[
        "Order ID",
        "Order Date",
        "Customer",
        "Country",
        "Region",
        "Product",
        "Category",
        "Quantity",
        "Unit Price",
        "Discount",
        "Sales",
        "Cost",
        "Profit",
        "Payment Method",
        "Sales Channel"
    ]
)

# Save dataset as CSV
df.to_csv(
    "ecommerce_sales_data.csv",
    index=False
)

# Display confirmation
print("Dataset created successfully!")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset saved as:")
print("ecommerce_sales_data.csv")