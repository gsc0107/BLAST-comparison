import numpy as np
import pandas as pd
import ml_metrics as metrics
import sys
from statistics import mean
from matplotlib import pyplot as plt
import os
from os import listdir

K =100 

def find_csv_filenames( path_to_dir, suffix=".csv" ): # input all files with csv format
    filenames = listdir(path_to_dir)
    return [ filename for filename in filenames if filename.endswith( suffix ) ]

df_list = []
files = find_csv_filenames(".","csv")
for file in files:
    print(file)
    df = pd.read_csv(file, sep='\t')
    print (df)
    df_list.append(df)
df = pd.concat(df_list)
df.columns = ['n', 'Blast', 'Diamond', 'Usearch', 'Mmseq2', 'UseLocal', 'BlastFast', 'k'] # change column name
r = pd.DataFrame(df).groupby(df.k).mean() # calculate MAPK

f = len(r.index) # identify column length
pd.options.display.max_rows = f
print (r)
r.to_csv('mean_Pre.csv')

blast = r['Blast']
blastf = r['BlastFast']
dia = r['Diamond']
use = r['Usearch']
mmseq = r['Mmseq2']
useloc = r['UseLocal']
k = r['k']
# build charts 
plt.plot(k, blast, color='green', linewidth = 2, label='Blast', alpha=0.4)
plt.plot(k, dia, color='red', linewidth = 2,  label='Diamond')
plt.plot(k, use, color='blue', linewidth = 2,  label='Usearch',alpha=0.4)
plt.plot(k, blastf, color='black', linewidth = 2, label='Blast-fast',alpha=0.4)
plt.plot(k, mmseq, color='pink', linewidth = 2, label='Mmseq2', alpha=0.4)
plt.plot(k, useloc, color='orange' , linewidth = 2, label='UseLocal', alpha=0.4)
plt.legend(loc = 'best')
plt.xlabel('k')
plt.ylabel('methods')
plt.title('Mean_Rec')
plt.savefig('Mean_rec.png')


