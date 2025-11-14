import pandas as pd
import numpy as np
import random

np.random.seed(0)
random.seed(0)

customers = pd.DataFrame({
    'customer_id': range(1, 101),
    'name': [f'Customer {i}' for i in range(1, 101)],
    'email': [f'customer{i}@example.com' for i in range(1, 101)]
})
customers.to_csv('customers.csv', index=False)

products = pd.DataFrame({
    'product_id': range(1, 21),
    'name': [f'Product {i}' for i in range(1, 21)],
    'price': np.random.uniform(10, 100, 20)
})
products.to_csv('products.csv', index=False)

orders = pd.DataFrame({
    'order_id': range(1, 101),
    'customer_id': np.random.choice(range(1, 101), 100),
    'order_date': pd.date_range('2022-01-01', periods=100)
})
orders.to_csv('orders.csv', index=False)

order_items = pd.DataFrame({
    'order_id': np.random.choice(range(1, 101), 200),
    'product_id': np.random.choice(range(1, 21), 200),
    'quantity': np.random.randint(1, 10, 200)
})
order_items.to_csv('order_items.csv', index=False)

payments = pd.DataFrame({
    'payment_id': range(1, 101),
    'order_id': range(1, 101),
    'payment_method': np.random.choice(['Credit Card', 'PayPal', 'Bank Transfer'], 100),
    'amount': np.random.uniform(10, 1000, 100)
})
payments.to_csv('payments.csv', index=False)
