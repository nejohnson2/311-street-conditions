import pandas as pd

'''
Read in original 311 file from https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9 and subset the data based on the 11222 Zip Code 

'''


# -- Import Original Data
print 'Reading in data...'
data = pd.read_csv('../Data/311_Service_Requests_from_2010_to_Present.csv')


# -- Subset Data
data = data[data['Incident Zip'] == 11222]


# -- Write data to file
print 'Writing new file...'
data.to_csv('../Data/11222.csv', index=False)