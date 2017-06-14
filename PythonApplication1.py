import numpy as np
import csv
import pandas as pd

filename = "test02.csv"

df = pd.read_csv(filename, sep=",", index_col=0)

#print (df)

print (df.index)

print (df[0:2])