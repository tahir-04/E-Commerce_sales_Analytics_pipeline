# scripts/extract.py

import pandas as pd

def load_csv(filepath):
    return pd.read_csv(filepath)

def extract_customers():
    return load_csv("data/raw/customers.csv")

def extract_orders():
    return load_csv("data/raw/orders.csv")

def extract_products():
    return load_csv("data/raw/products.csv")

def extract_payments():
    return load_csv("data/raw/payments.csv")

def extract_sellers():
    return load_csv("data/raw/sellers.csv")

def extract_order_items():
    return load_csv("data/raw/order_items.csv")

def extract_order_payments():
    return load_csv("data/raw/order_payments.csv")

def extract_order_reviews():
    return load_csv("data/raw/order_reviews.csv")

def extract_geolocation():
    return load_csv("data/raw/geolocation.csv")