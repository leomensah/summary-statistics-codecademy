import numpy as np
import pandas as pd
from scipy.stats import pearsonr, chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns

import codecademylib3
np.set_printoptions(suppress=True, precision = 2)

nba = pd.read_csv('./nba_games.csv')

# Subset Data to 2010 Season, 2014 Season
nba_2010 = nba[nba.year_id == 2010]
nba_2014 = nba[nba.year_id == 2014]

print(nba_2010.head())
print(nba_2014.head())

knicks_pts = nba_2010.pts[nba_2010.fran_id == 'Knicks']
nets_pts = nba_2010.pts[nba_2010.fran_id == 'Nets']

print(nets_pts)

knicks_mean_score = np.mean(knicks_pts)
nets_mean_score = np.mean(nets_pts)
diff_means = knicks_mean_score - nets_mean_score
print(diff_means)


plt.hist(knicks_pts, alpha = 0.5, normed=True, label='Knicks')
plt.hist(nets_pts, alpha = 0.5, normed=True, label='nets')
plt.legend()
plt.show()



knicks_2014_pts = nba_2014.pts[nba_2014['fran_id'] == 'Knicks']
nets_2014_pts = nba_2014.pts[nba_2014['fran_id'] == 'Nets']

knicks_2014_mean = np.mean(knicks_2014_pts)
nets_2014_mean = np.mean(nets_2014_pts)

diff_means_2014 = knicks_2014_mean - nets_2014_mean
print(diff_means_2014)

plt.hist(knicks_2014_pts, alpha=0.5, label='Knicks', normed=True)
plt.hist(nets_2014_pts, alpha=0.5, label='Nets', normed=True)
plt.show()

sns.boxplot(nba_2010.fran_id, nba_2010.pts)
plt.show()
plt.clf()
location_result_freq = pd.crosstab(nba_2010.game_result, nba_2010.game_location)
print(location_result_freq)

location_result_proportions = location_result_freq / len(nba_2010)

print(location_result_proportions)

chi2, pval, dof, expected = chi2_contingency(location_result_freq)
print(expected)
print(chi2)

nba_2010_cov_forecast_point_diff = np.cov(nba_2010.forecast, nba_2010.point_diff)
print(nba_2010_cov_forecast_point_diff)


forecast_point_diff_correlation = pearsonr(nba_2010.forecast, nba_2010.point_diff)
print(forecast_point_diff_correlation)


plt.scatter(nba_2010.forecast, nba_2010.point_diff)
plt.show()