import pandas as pd

df = pd.read_csv(
    "data/raw/customers.csv"
)

print(df.head())
print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.isnull().sum())

duplicates = df.duplicated().sum()
print(duplicates)

orders = pd.read_csv(
    "data/raw/orders.csv"
)
print(orders.head())

orders[
    "order_purchase_timestamp"
] = pd.to_datetime(
    orders["order_purchase_timestamp"]
)

print(
    orders.dtypes
)

items = pd.read_csv(
    "data/raw/order_items.csv"
)
print(items.head())
print(items.dtypes)

products = pd.read_csv(
    "data/raw/products.csv"
)
print(products.head())
print(products.dtypes)  
print(products.columns)
print(products.shape)

payments = pd.read_csv(
    "data/raw/order_payments.csv"
)
print(payments.head())
print(payments.dtypes)

sellers = pd.read_csv(
    "data/raw/sellers.csv"
)
print(sellers.head())
print(sellers.dtypes)