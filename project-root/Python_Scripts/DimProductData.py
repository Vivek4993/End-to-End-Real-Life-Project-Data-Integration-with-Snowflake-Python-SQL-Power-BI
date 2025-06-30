#import python libraries
import pandas as pd
import csv
import random
import os


directory="D:/Vivek/PROJECTS/SNOWFLAKE_SQL_PYTHON_POWERBI_PROJECT/One_Time_Lead/DimProduct/"

## input the number of rows  that the csv file should pocess

num_rows_req= int(input("Enter the number of rows the  csv file should have: "))




## input the name ofthe csv file ( for example data_cust.csv)

csv_file_name= input("Enter the name of the csv file like data_cust.csv :")


## Full csv file name and file path

full_file_path = os.path.join(directory,csv_file_name)


##
excel_file_path_name="D:/Vivek/PROJECTS/SNOWFLAKE_SQL_PYTHON_POWERBI_PROJECT/Project_Lookup_File.xlsx"
excel_sheet_name_product= "Product_Names"
product_column_name= "product names"
excel_sheet_name_category= "Product_Categories"
category_column_name= "Category Name"

## Creating data frames

df_product=  pd.read_excel(excel_file_path_name, sheet_name= excel_sheet_name_product)
df_category= pd.read_excel(excel_file_path_name, sheet_name=excel_sheet_name_category)


##  create the header required f or the csv  file name

header= ['ProductName', 'Category', 'Brand', 'UnitPrice']



# Create list to store rows
data_rows = []

##Loop and geenerate multiple rows
for _ in range(num_rows_req):
    row=[
        df_product[product_column_name].sample(n=1).values[0], ## Product Name
        df_category[category_column_name].sample(n=1).values[0],  ## Category name
        random.choice(['Samsung','Philips','BlackDecker','Coleman','Apple','Nike','Ford','Coca-Cola']),
        random.randint(100,1000)
    ]
    data_rows.append(row)
# Create DataFrame
    df = pd.DataFrame(data_rows, columns=header)

# Print the DataFrame
    print(df)
# Save DataFrame to CSV
    df.to_csv(full_file_path, index=False)

## printing the sucess statment
print(f"{num_rows_req} rows of the dake data have been written to: {full_file_path} ")

##