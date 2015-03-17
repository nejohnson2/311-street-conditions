import pandas as pd

'''
A script to subset the data based on a select number of complaint types.
'''

data = pd.read_csv('../Data/11222.csv')

# -- Select Conditions to subset
items = ['Street Condition', 'Sidewalk Condition', 'Dirty Conditions', 'Missed Collection (All Materials)', 'Sanitation Condition', 'Derelict Vehicles', 'Derelict Vehicle', 'Recycling Enforcement', 'Industrial Waste', 'Vacant Lot', 'Root/Sewer/Sidewalk Condition', 'Litter Basket / Request', 'Hazardous Materials', 'Overflowing Litter Baskets', 'Derelict Bicycle', 'Curb Condition', 'Adopt-A-Basket', 'Sweeping/Missed', 'Overflowing Recycling Baskets', 'Sweeping/Missed-Inadequate']


# -- Subset data
data = data[data['Complaint Type'].isin(items)]


# -- Write File
data.to_csv('../Data/11222_subset.csv', index=False)