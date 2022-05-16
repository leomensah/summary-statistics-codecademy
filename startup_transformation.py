import codecademylib3
from sklearn import preprocessing
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# load in financial data
financial_data = pd.read_csv('financial_data.csv')
expense_overview = pd.read_csv('expenses.csv')

# code goes here
# print(financial_data.head())
# print(financial_data.dtypes)
print(expense_overview.head())

month = financial_data['Month']
revenue = financial_data['Revenue']
expenses = financial_data['Expenses']

plt.plot(month, revenue)
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.title('Revenue')
plt.show()

plt.clf()

plt.plot(month, expenses)
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.title('Expenses')
plt.show()

expense_categories = expense_overview['Expense']
proportions = expense_overview['Proportion']
plt.clf()
plt.pie(proportions, labels = expense_categories)
plt.title('Pie Chart showing expenses')
plt.axis('Equal')
plt.tight_layout()
plt.show()

expense_categories = ['Salaries', 'Advertising', 'Office Rent', 'Other']
proportions = [0.62, 0.15, 0.15, 0.08]
plt.clf()
plt.pie(proportions, labels = expense_categories)
plt.title('Expense Categories')
plt.axis('Equal')
plt.tight_layout()
plt.show()

expense_cut = 'Salaries'
employees = pd.read_csv('employees.csv')
print(employees.head())

sorted_productivity = employees.sort_values(by=['Productivity'])
print(sorted_productivity)

employees_cut = sorted_productivity.head(100)
print(employees_cut)

transformation = 'staradardization'
commute_times = employees['Commute Time']

print(commute_times.describe())
plt.clf()
plt.hist(commute_times)
plt.show()

commute_times_log = np.log(commute_times)
plt.clf()
plt.hist(commute_times_log)
plt.show()