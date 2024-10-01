import pooch
import urllib.request
import csv
import pandas as pd
import numpy as np

#url = 'https://unils-my.sharepoint.com/:x:/g/personal/tom_beucler_unil_ch/ETDZdgCkWbZLiv_LP6HKCOAB2NP7H0tUTLlP_stknqQHGw?e=2lFo1x'

datafile = pooch.retrieve('https://unils-my.sharepoint.com/:x:/g/personal/tom_beucler_unil_ch/ETDZdgCkWbZLiv_LP6HKCOAB2NP7H0tUTLlP_stknqQHGw?download=1',
                          known_hash='c7676360997870d00a0da139c80fb1b6d26e1f96050e03f2fed75b921beb4771')

row = [] # Initializes row to an empty list
with open(datafile, 'r') as fh:
  reader = csv.reader(fh)
  for info in reader:
    row.append(info)

def output_monthindices(month=None):
  """
  This function takes a string "month" as input (e.g., January)
  and outputs the first and last indices of that month
  """
  test = [rowobj[1].split(' ')[0].split('-')[1] for rowobj in row[1:]]
  truefalse = []
  for obj in test:
    if obj==month:
      truefalse.append(obj)
    else:
      truefalse.append(np.nan)
  return pd.Series(truefalse).first_valid_index(),pd.Series(truefalse).last_valid_index()



  # Here, we output the first and last indices of Jan/Feb/Mar
Jan_index = output_monthindices(month='01')
Feb_index = output_monthindices(month='02')
Mar_index = output_monthindices(month='03')


savefile = ["jan.csv", "feb.csv", "mar.csv"] # List containing the filenames
indices = [Jan_index, Feb_index, Mar_index]
for i in range(len(savefile)):
  with open(savefile[i], 'w') as fh:
    writer = csv.writer(fh)
    for num in range(indices[i][0],indices[i][1]):
      writer.writerow(row[num])


#@title Let's print the dates in March
df = pd.read_csv(savefile[0]) # Reads the file using pandas
df.head(10) # Print the first three lines of the file