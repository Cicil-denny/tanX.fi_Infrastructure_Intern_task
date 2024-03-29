# -*- coding: utf-8 -*-
"""tanX.fi - Infrastructure Intern task.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JI0U5NP_o0VOPJY_4vGdB2Xfhop_cBli

**Infrastructure Engineer Internship taks**

Problem Statement: Python code to analyse the CSV file on orders.csv

1. Creation of CSV file for analysis with random values...
"""

import csv

csv_content = """order_id,customer_id,order_date,product_id,product_name,product_price,quantity
1,C100,2022-01-01,P001,Product A,20.99,3
2,C101,2022-01-02,P002,Product B,15.49,2
3,C102,2022-01-03,P003,Product C,30.00,1
4,C103,2022-01-04,P004,Product D,25.99,4
5,C104,2022-01-05,P005,Product E,10.00,2
6,C105,2022-02-01,P001,Product A,20.99,3
7,C106,2022-02-02,P002,Product B,15.49,2
8,C107,2022-02-03,P003,Product C,30.00,1
9,C108,2022-02-04,P004,Product D,25.99,4
10,C109,2022-02-05,P005,Product E,10.00,2
11,C110,2022-03-01,P001,Product A,20.99,3
12,C111,2022-03-02,P002,Product B,15.49,2
13,C112,2022-03-03,P003,Product C,30.00,1
14,C113,2022-03-04,P004,Product D,25.99,4
15,C114,2022-03-05,P005,Product E,10.00,2
16,C115,2022-04-01,P001,Product A,20.99,3
17,C116,2022-04-02,P002,Product B,15.49,2
18,C117,2022-04-03,P003,Product C,30.00,1
19,C118,2022-04-04,P004,Product D,25.99,4
20,C119,2022-04-05,P005,Product E,10.00,2
21,C120,2022-05-01,P001,Product A,20.99,3
22,C121,2022-05-02,P002,Product B,15.49,2
23,C122,2022-05-03,P003,Product C,30.00,1
24,C123,2022-05-04,P004,Product D,25.99,4
25,C124,2022-05-05,P005,Product E,10.00,2
26,C125,2022-06-01,P001,Product A,20.99,3
27,C126,2022-06-02,P002,Product B,15.49,2
28,C127,2022-06-03,P003,Product C,30.00,1
29,C128,2022-06-04,P004,Product D,25.99,4
30,C129,2022-06-05,P005,Product E,10.00,2
31,C130,2022-07-01,P001,Product A,20.99,3
32,C131,2022-07-02,P002,Product B,15.49,2
33,C132,2022-07-03,P003,Product C,30.00,1
34,C133,2022-07-04,P004,Product D,25.99,4
35,C134,2022-07-05,P005,Product E,10.00,2
36,C135,2022-08-01,P001,Product A,20.99,3
37,C136,2022-08-02,P002,Product B,15.49,2
38,C137,2022-08-03,P003,Product C,30.00,1
39,C138,2022-08-04,P004,Product D,25.99,4
40,C139,2022-08-05,P005,Product E,10.00,2
41,C140,2022-09-01,P001,Product A,20.99,3
42,C141,2022-09-02,P002,Product B,15.49,2
43,C142,2022-09-03,P003,Product C,30.00,1
44,C143,2022-09-04,P004,Product D,25.99,4
45,C144,2022-09-05,P005,Product E,10.00,2
46,C145,2022-10-01,P001,Product A,20.99,3
47,C146,2022-10-02,P002,Product B,15.49,2
48,C147,2022-10-03,P003,Product C,30.00,1
49,C148,2022-10-04,P004,Product D,25.99,4
50,C149,2022-10-05,P005,Product E,10.00,2
"""

# Writing to CSV file
with open('orders.csv', 'w', newline='') as csvfile:
    csvfile.write(csv_content)

print("CSV file 'orders.csv' created successfully!")

"""2. CSV file analysis"""

import pandas as pd
from datetime import datetime

# Read CSV file
df = pd.read_csv(r'/content/orders.csv')

# Convert 'order_date' to datetime format
df['order_date'] = pd.to_datetime(df['order_date'])

"""3. Python approach on csv"""

# Task 1: Compute total revenue generated by the online store for each month
df['order_month'] = df['order_date'].dt.to_period('M')
monthly_revenue = df.groupby('order_month')['product_price'].sum()

# Task 2: Compute total revenue generated by each product
product_revenue = df.groupby('product_name')['product_price'].sum()

# Task 3: Compute total revenue generated by each customer
customer_revenue = df.groupby('customer_id')['product_price'].sum()

# Task 4: Identify the top 10 customers by revenue
top_customers = customer_revenue.sort_values(ascending=False).head(10)

"""4. Displaying the results"""

# Display results
print("Task - 1: \nTotal Revenue by Month:")
print(monthly_revenue)

print("\nTask - 2: \nTotal Revenue by Product:")
print(product_revenue)

print("\nTask - 3: \nTotal Revenue by Customer:")
print(customer_revenue)

print("\nTask - 4: \nTop 10 Customers by Revenue:")
print(top_customers)

"""5. Pandas and Matplotlib for data analysis and visualization"""

# Display basic statistics of the dataset
import matplotlib.pyplot as plt

print("Basic Statistics:\n", df.describe())

# Plotting total revenue by product
product_revenue = df.groupby('product_name')['product_price'].sum()
product_revenue.plot(kind='bar', title='Total Revenue by Product')
plt.xlabel('Product')
plt.ylabel('Total Revenue')
plt.show()

"""Analysis:

         Product C is the highest revenue-generating product, followed by Product D and Product A.

         Product E is the lowest revenue-generating product.

         There is a significant difference in revenue between the top-performing products and the bottom-performing products.











"""

# Average Order Value for Each Product
avg_order_value = df.groupby('product_name')['product_price'].mean()

"""6. Trying to add another new Column 'cost_price' to analyse even more"""

import random
from datetime import datetime, timedelta

# Generating random data for demonstration
def generate_random_data():
    order_id = random.randint(1000, 9999)
    customer_id = random.randint(1, 50)
    order_date = datetime.now() - timedelta(days=random.randint(1, 365))
    product_id = random.randint(1, 10)
    product_name = f'product{product_id}'
    product_price = random.uniform(10, 100)
    quantity = random.randint(1, 10)
    return order_id, customer_id, order_date, product_id, product_name, product_price, quantity

# Creating a list of 50 entities
data = [generate_random_data() for _ in range(50)]

# Creating a DataFrame
columns = ['order_id', 'customer_id', 'order_date', 'product_id', 'product_name', 'product_price', 'quantity']
df = pd.DataFrame(data, columns=columns)

# Assuming a fixed cost for each product (you can replace this with actual cost data)
product_cost = {'product1': 5, 'product2': 8, 'product3': 10, 'product4': 6, 'product5': 12}

# Adding 'cost_price' column based on the fixed cost dictionary
df['cost_price'] = df['product_name'].map(product_cost)

# Save the DataFrame with the new column to a new CSV file
df.to_csv('orders_with_cost_50_entities.csv', index=False)

# Profit Margin for Each Product
# Assuming 'cost_price' column is available in the DataFrame
df['profit_margin'] = (df['product_price'] - df['cost_price']) / df['product_price']

# Display the results
print("Average Order Value:\n", avg_order_value)
print("\nProfit Margin:\n", df.groupby('product_name')['profit_margin'].mean())

"""Analysis:

    Product C has the highest average order value, indicating it is priced higher compared to others.

    Product 1 and Product 4 have the highest profit margins, suggesting these products are more profitable.
    
    Product B has a lower average order value and profit margin, potentially indicating a lower-priced or less profitable item.
"""

