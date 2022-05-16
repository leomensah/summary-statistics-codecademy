import pandas as pd
import numpy as np

car_eval = pd.read_csv('car_eval_dataset.csv')
print(car_eval.head())

print(car_eval['manufacturer_country'].value_counts())

print(car_eval['manufacturer_country'].value_counts(normalize=True))

print(car_eval['buying_cost'].unique())
buying_cost_categories = ['low', 'med', 'high', 'vhigh']

car_eval['buying_cost'] = pd.Categorical(car_eval['buying_cost'], buying_cost_categories, ordered=True)

buying_index = np.median(car_eval['buying_cost'].cat.codes)

buying_cost_median_category = buying_cost_categories[int(buying_index)]

print(buying_cost_median_category)

print(car_eval['luggage'].value_counts(normalize=True))

print(car_eval['luggage'].value_counts(dropna = False, normalize=True))

print(car_eval['doors'] == '5more')

print((car_eval['doors'] == '5more').value_counts(normalize=True))
