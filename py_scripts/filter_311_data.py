import pandas as pd

```
Read in original 311 file from https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9 and subset the data based on the 11222 Zip Code and a series of Complaint Types

```


# -- Import Original Data
data = pd.read_csv('../Data/')


# -- Select Conditions to subset
items = ['Street Condition', 'Sidewalk Condition', 'Dirty Conditions', 'Missed Collection (All Materials)', 'Sanitation Condition', 'Derelict Vehicles', 'Derelict Vehicle', 'Recycling Enforcement', 'Industrial Waste', 'Vacant Lot', 'Root/Sewer/Sidewalk Condition']


# -- Subset Data
data = data[(data['incident_zip'] == 11222) & (data['complaint_type'].isin(items))]


# -- Write data to file
data.to_csv('../Data/311-Street-Conditions.csv', index=False)