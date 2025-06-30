## Python libraries required  for creating fact table


import pandas as pd
import numpy as np
import os

## Asking the user to enter the number od rows to be generaated

DateID='20240904'
directory="D:/Vivek/PROJECTS/SNOWFLAKE_SQL_PYTHON_POWERBI_PROJECT/landing_directory"


## DateID  ProductID StoreID CustomerID QuantityOrdered OrderAmount DiscountAmount 

for i in range (1,101):
    num_rows_req= np.random.randint(100,1000)
    data= {
        'DateID': ['DATEID']* num_rows_req,
        'ProductID': np.random.randint(1, 1001, size=num_rows_req),
        'StoreID': [i]* num_rows_req,
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
    df['shipping_cost'] = df['OrderAmount']* shipping_cost  
    df['TotalAmount']= df['OrderAmount']-df['DiscountAmount']+df['shipping_cost']

    file_name= f'Store_{i}_{DateID}.csv'
    file_path= os.path.join(directory,file_name)

##If  file exists remove  and write again
    if os.path.exists(file_path):
        os.remove(file_path)
    

    df.to_csv(file_path,index=False)
