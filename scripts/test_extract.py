# scripts/test_extract.py

from extract import extract_customers

customers = extract_customers()

print(customers.head())
print(customers.shape)
print(customers.columns)
print(customers.info())
print(customers.isnull().sum())