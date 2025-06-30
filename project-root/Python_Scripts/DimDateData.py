## importing pythong  libraries

import pandas as pd
import numpy as np
import os

directory="D:/Vivek/PROJECTS/SNOWFLAKE_SQL_PYTHON_POWERBI_PROJECT/One_Time_Lead/DimDate/"
file_name = "DimDateData.csv"
full_file_path = os.path.join(directory, file_name)

## start and end data between which we need to geenrate our dates

start_date = '2014-01-01'

end_date = '2025-05-31'


## Generate a seies of datesbetwe start and end dates

date_range= pd.date_range(start=start_date, end= end_date)
print(date_range)

## Randomly sample 5,000 dates (with replacement if necessary)
sampled_dates = np.random.choice(date_range, size=5000, replace=True)


## Convert these series of dates into a  data frame

date_dim = pd.DataFrame(sampled_dates,  columns= ['Date'])
print(date_dim)

## Add new column to our dataframe

date_dim['DayofWeek'] = date_dim['Date'].dt.dayofweek
date_dim['Month'] =date_dim['Date'].dt.month
date_dim['Quarter'] =date_dim['Date'].dt.quarter

date_dim['Year'] =date_dim['Date'].dt.year
date_dim['Isweekend'] =date_dim['DayofWeek'].isin([5,6])
date_dim['DateID']= date_dim['Date'].dt.strftime('%Y%m%d').astype(int)
print(date_dim)

##Reorder our data frame so that the dataid becomes the 1st column

cols= ['DateID'] +[col for col in date_dim.columns if col!= 'DateID']
print(cols)

date_dim= date_dim[cols]


##Save to CSV to a file path given
date_dim.to_csv(full_file_path, index=False)

# Print confirmation
print(f"\n 5000 random date dimension rows saved to: {full_file_path}")