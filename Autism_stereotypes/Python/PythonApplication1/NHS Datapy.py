import pandas as pd
import matplotlib .pyplot as plt
import statistics
import csv

# Read the CSV file into a DataFrame
Autismdatabase = pd.read_csv("England.csv")

# Plotting
Autismdatabase.plot(x='Gender', y='Total', kind='bar')
plt.title('Gender 2018-2019 Q3')
plt.xlabel('Gender')
plt.ylabel('Total')
plt.show()