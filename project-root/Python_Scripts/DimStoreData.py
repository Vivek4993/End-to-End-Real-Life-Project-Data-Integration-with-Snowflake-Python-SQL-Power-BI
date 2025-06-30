#import python libraries
import pandas as pd
import csv
import random
from faker import Faker
import os

directory="D:/Vivek/PROJECTS/SNOWFLAKE_SQL_PYTHON_POWERBI_PROJECT/One_Time_Lead/DimStore/"

## intitlization of faker to generate random data

fake=Faker()


## input the number of rows  that the csv file should pocess

num_rows_req= int(input("Enter the number of rows the  csv file should have: "))




## input the name ofthe csv file ( for example data_cust.csv)

csv_file_name= input("Enter the name of the csv file like data_cust.csv :")

## Full filename and file path

full_file_path = os.path.join(directory,csv_file_name)



## Details of the excel file that has the lookup data,  file path and name, sheet name and column  names  where the data is present

excel_file_path_name="D:/Vivek/PROJECTS/SNOWFLAKE_SQL_PYTHON_POWERBI_PROJECT/Project_Lookup_File.xlsx"
excel_sheet_name= "Store_Name_Data"
adjective_column_name= "Adjectives"
noun_column_name= "Nouns"

## Fetch this sheet  data ina dataframe

df1= pd.read_excel(excel_file_path_name,sheet_name=excel_sheet_name)

print(df1)


##  create the header required f or the csv  file name

header= ['StoreName', 'StoreType', 'StoreOpeningDate','Address', 'City','State','ZipCode', 'Country','Region', 'Manager Name']


# Create list to store rows
data_rows = []

##Loop and geenerate multiple rows
for _ in range(num_rows_req):
    random_adjectives=df1[adjective_column_name].sample(n=1).values[0]
    random_noun=df1[noun_column_name].sample(n=1).values[0]
    store_name=f"The {random_adjectives} {random_noun}"
    print(store_name)
    row=[
        store_name,
        random.choice(['Exclusive','MBO','SMB','Outlet Stores']),
        fake.date(),
        fake.address().replace(","," ").replace("\n"," "),
        fake.city(),
        fake.state(),
        fake.postcode(),
        fake.country(),
        random.choice(['West','East','North','South']),
        fake.first_name()
    ]
    data_rows.append(row)
# Create DataFrame
    df = pd.DataFrame(data_rows, columns=header)

# Print the DataFrame
    print(df)
# Save DataFrame to CSV
    df.to_csv(full_file_path, index=False)
print(f"{num_rows_req} rows of the dake data have been written to: {full_file_path} ")

##