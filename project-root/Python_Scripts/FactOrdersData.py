## Python libraries required  for creating fact table


import pandas as pd
import numpy as np
import os


directory="D:/Vivek/PROJECTS/SNOWFLAKE_SQL_PYTHON_POWERBI_PROJECT/One_Time_Lead/FactOrders/"

## Aksing the user to enter the number od rows to be generaated

num_rows_req= int(input("Ente the no fo rows to be generated :"))

## DateID  ProductID StoreID CustomerID QuantityOrdered OrderAmount DiscountAmount 


## input the name ofthe csv file ( for example data_cust.csv)

csv_file_name= input("Enter the name of the csv file like data_cust.csv :")


## Full filename and file path
full_file_path = os.path.join(directory,csv_file_name)


## Generate random dates between 2014-01-01 and 2025-05-31
date_random_series = np.random.choice(np.arange(np.datetime64('2014-01-01'), np.datetime64('2025-05-31')),size=num_rows_req)


print(date_random_series)


formatted_rows= pd.to_datetime(date_random_series).strftime('%Y%m%d')
print(formatted_rows)

data= {
    'DateID': formatted_rows,
    'ProductID': np.random.randint(1, 1001, size=num_rows_req),
    'StoreID': np.random.randint(1, 101, size=num_rows_req),
    'CustomerID': np.random.randint(1, 1001, size=num_rows_req),
    'QuantityOrdered': np.random.randint(1, 21, size=num_rows_req),
    'OrderAmount': np.random.randint(100, 1001, size=num_rows_req)
    }
print(data)

df= pd.DataFrame(data)
print(df)

## discount  percent bcne be bneter 2 and 15 percent percent    we weill usilsie numpy random uniform and we kniw the shipping cost is between 5 qand 15 percent

discount_perc = np.random.uniform(0.02, 0.15, size=num_rows_req)
shipping_cost = np.random.uniform(0.05,0.15, size=num_rows_req)


## Calculate column

df['DiscountAmount'] = df['OrderAmount'] * discount_perc

## Shipping Cost and  TotalAmount
df['shipping_cost'] = df['OrderAmount']* shipping_cost
df['TotalAmount']= df['OrderAmount']-df['DiscountAmount']+df['shipping_cost']

##Save to CSV to a file path given
df.to_csv(full_file_path, index=False)

# Print confirmation
print(f"\n random fact order dimension rows saved to: {full_file_path}")