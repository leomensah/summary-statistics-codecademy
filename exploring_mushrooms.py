import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import codecademylib3

# load in the data
df = pd.read_csv("mushroom_data.csv")
print(df.head())

# list of all column headers
columns = df.columns.tolist()
# for col in df:
#   print('name of column is: ',col,': and unique values: ', df[col].unique())

for column in columns:
  print(column)

for column in columns:
  #print(column)
  sns.countplot(df[column], order=df[column].value_counts().index)
  plt.title(column + " Value Counts")
  plt.xticks(rotation=30, fontsize=10)
  plt.xlabel(column, fontsize=12)
  plt.show()
  plt.clf()