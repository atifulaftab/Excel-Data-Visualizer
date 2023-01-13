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

print("Select Option from the below\n")
print("Bar\n")
print("Scatter\n")
print("Regular\n")
print("Stem\n")
print("Fill\n")
print("Stackplot\n")
print("All\n")
choice=input("Type your Selection Exactly\n")


if choice == "All":
    fig1=plt.bar(df.loc[:,col1],df.loc[:,col2])
    fig2=plt.scatter(df.loc[:,col1],df.loc[:,col2])
    fig3=plt.plot(df.loc[:,col1],df.loc[:,col2])
    fig4=plt.stem(df.loc[:,col1],df.loc[:,col2])
    fig5=plt.fill_between(df.loc[:,col1],df.loc[:,col2])
    fig6=plt.stackplot(df.loc[:,col1],df.loc[:,col2])
elif choice == "Bar":
    fig1=plt.bar(df.loc[:,col1],df.loc[:,col2])
elif choice == "Scatter":
    fig2=plt.scatter(df.loc[:,col1],df.loc[:,col2])
elif choice == "Regular":
    fig3=plt.plot(df.loc[:,col1],df.loc[:,col2])
elif choice == "Stem":
    fig4=plt.stem(df.loc[:,col1],df.loc[:,col2])
elif choice == "Fill":
    fig5=plt.fill_between(df.loc[:,col1],df.loc[:,col2])
elif choice == "Stackplot":
    fig6=plt.stackplot(df.loc[:,col1],df.loc[:,col2])
else:
    print("Wrong Input")

print("Done")