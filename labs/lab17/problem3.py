import pandas as pd

games = pd.read_csv(input(), sep=';')
rates = pd.read_csv(input(), sep=';')

rates_d = []
n = len(list(games.iterrows()))
for i in range(n):
    rates_d.append(rates[rates['id'] == (i + 1)]['mark'].mean())

games['mean'] = rates_d
games.head()

games_sorted = games.sort_values(by='mean', ascending=False).head(3)

name = games['name']
mean = games['mean']

for i in games_sorted.iterrows():
    temp_1 = name.iloc[i[0]]
    temp_2 = mean.iloc[i[0]]
    print(temp_1, f"{round(temp_2, 3):.3f}")

otl_games = games[mean > 8.0]
otl_grouped = pd.DataFrame(otl_games.groupby('company')['name'].count())
otl_grouped = otl_grouped.sort_values(by='name', ascending=False)

print(otl_grouped.index[0], otl_grouped['name'][0])