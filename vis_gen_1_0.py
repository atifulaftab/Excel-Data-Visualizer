#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 23:00:47 2023

@author: atifulaftab
"""

import pandas as pd
import matplotlib.pyplot as plt


filename=input("Enter your file name\n")
#filename="data.xlsx"
df= pd.read_excel(filename)
col=df.head()
print("*************************************\n")
print("List of Columns\n")
for column in df.columns:
    print(column)
print("*************************************\n")

col1=input("Enter First column\n")
col2=input("Enter Second column\n")
print("*************************************\n")
print("Generating Plots\n")

plt.bar(df.loc[:,col1],df.loc[:,col2])

print("Done")