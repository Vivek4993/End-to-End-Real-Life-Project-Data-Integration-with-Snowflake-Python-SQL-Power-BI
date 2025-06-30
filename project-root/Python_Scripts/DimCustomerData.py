#import python libraries
import pandas as pd
import csv
import random
from faker import Faker
import os



directory="D:/Vivek/PROJECTS/SNOWFLAKE_SQL_PYTHON_POWERBI_PROJECT/One_Time_Lead/DimCustomer/"

## intitlization of faker to generate random data

fake=Faker()


## input the number of rows  that the csv file should pocess

num_rows_req= int(input("Enter the number of rows the  csv file should have: "))




## input the name ofthe csv file ( for example data_cust.csv)

csv_file_name= input("Enter the name of the csv file like data_cust.csv :")


## Full filename and file path

full_file_path = os.path.join(directory,csv_file_name)


##  create the header required f or the csv  file name

header= ['First Name', 'Last Name', 'Gender','DateOfBirth','Email','PhoneNumber','Address', 'City','State', 'ZipCode', 'Country', 'LoyalityProgranID']


# Create list to store rows
data_rows = []


##Loop and geenerate multiple rows
for _ in range(num_rows_req):
    row=[
        fake.first_name(),
        fake.last_name(),
        random.choice(['M','F','Others','Not Specidied']),
        fake.date(),
        fake.email(),
        fake.phone_number(),
        fake.address().replace(","," ").replace("\n"," "),
        fake.city(),
        fake.state(),
        fake.postcode(),
        fake.country(),
        random.randint(1,5)
    ]
    data_rows.append(row)
# Create DataFrame
df = pd.DataFrame(data_rows, columns=header)

# Print the DataFrame
print(df)
# Save DataFrame to CSV
df.to_csv(full_file_path, index=False)

print(f"\n✅ {num_rows_req} rows of fake data have been saved to: {full_file_path}")
        


##