
import codecademylib3_seaborn
import pandas as pd
from matplotlib import pyplot as plt

healthcare = pd.read_csv("healthcare.csv")
print(healthcare.head())

#print(healthcare["DRG Definition"].unique())
chest_pain = healthcare[healthcare['DRG Definition'] == '313 - CHEST PAIN']

# Getting every chest pain diagnosis in Alabama
alabama_chest_pain = chest_pain[chest_pain['Provider State'] == "AL"]

# Get values of Average Covered Charges in Alabama
costs = alabama_chest_pain[' Average Covered Charges '].values
print(costs)

# Getting all the states in the chest pain data
states = chest_pain['Provider State'].unique()
# print(states)

datasets = []
for state in states:
  datasets.append(chest_pain[chest_pain['Provider State'] == state][' Average Covered Charges '].values)


plt.figure(figsize=(20,6))
plt.boxplot(datasets, labels=states)
plt.show()
