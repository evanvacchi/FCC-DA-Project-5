import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv('epa-sea-level.csv')
pd.set_option('display.max_columns', None)
print(df.head())

plt.scatter(x='Year', y='CSIRO Adjusted Sea Level', data=df)

res = stats.linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
x = list(range(1880, 2050))
y = list()
for year in x:
    y.append(res.intercept + res.slope*year)
# res = stats.linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
# plt.plot(df['Year'], res.intercept + res.slope*df['Year'], 'r')
plt.plot(x,y,'r') #first line of best fit

df2 = df.loc[df.Year >= 2000]
# print(df2)
nres = stats.linregress(df2['Year'], df2['CSIRO Adjusted Sea Level'])
nx = list(range(2000, 2050))
ny = list()
for year in nx:
    ny.append(nres.intercept + nres.slope*year)
plt.plot(nx, ny, 'r') #second line of best fit


plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')

plt.savefig('sea_level_plot.png')

def draw_plot():
    # Read data from file


    # Create scatter plot


    # Create first line of best fit


    # Create second line of best fit


    # Add labels and title


    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
