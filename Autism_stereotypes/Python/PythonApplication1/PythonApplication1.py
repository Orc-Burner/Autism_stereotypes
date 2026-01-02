import pandas as pd
import matplotlib .pyplot as plt
import statistics
import csv

# Read the CSV file into a DataFrame
Autismdatabase = pd.read_csv("Age.csv")

# Plotting
Autismdatabase.plot(x='Age', y='Q1', kind='bar')
plt.title('First quarter')
plt.xlabel('Age')
plt.ylabel('Q1')
plt.show()
