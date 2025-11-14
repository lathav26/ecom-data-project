import pandas as pd
import sqlite3

conn = sqlite3.connect('ecom.db')
cursor = conn.cursor()

for file in ['customers', 'products', 'orders', 'order_items', 'payments']:
    df = pd.read_csv(f'{file}.csv')
    df.to_sql(file, conn, if_exists='replace', index=False)

conn.commit()
conn.close()
