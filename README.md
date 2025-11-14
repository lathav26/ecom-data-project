A complete end-to-end mini data engineering workflow built using Python, Pandas, SQLite, and SQL.
This project generates synthetic e-commerce data, ingests it into a SQLite database, and performs analytical SQL queries.

This project includes:

1. Synthetic Data Generation

Generates 5 datasets using Python:

customers.csv

products.csv

orders.csv

order_items.csv

payments.csv

All data is randomly generated for demo and testing purposes.

 2. SQLite Database Ingestion

Uses ingest_data.py to load all CSV files into ecom.db with tables:

customers

products

orders

order_items

payments

3. SQL Analysis

Includes a SQL join query (query.sql) that combines data from all tables to produce:

customer name

product name

order date

quantity

price

total amount

4. Final Query Output

Sample output from the JOIN query is stored in results.txt.

📁 Project Structure
ecom-data-project/
│
├── customers.csv
├── products.csv
├── orders.csv
├── order_items.csv
├── payments.csv
│
├── generate_data.py
├── ingest_data.py
├── query.sql
├── results.txt
│
├── ecom.db
└── README.md
