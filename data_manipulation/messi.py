
import pandas as pd


data = {
    'Season': ['2017-2018', '2018-2019', '2019-2020', '2020-2021', '2021-2022'],
    'Goals': [45, 51, 31, 38, 24],  # Number of goals scored in each season
    'Assists': [12, 19, 21, 9, 13]   # Number of assists in each season
}


df = pd.DataFrame(data)

print("Messi's Goal and Assist Stats by Season:")
print(df)


avg_goals = df['Goals'].mean()
avg_assists = df['Assists'].mean()
print("\nAverage Goals per Season:", avg_goals)
print("Average Assists per Season:", avg_assists)

max_goals_season = df.loc[df['Goals'].idxmax()]
print("\nSeason with the Most Goals:")
print(max_goals_season)


total_goals = df['Goals'].sum()
total_assists = df['Assists'].sum()
print("\nTotal Goals:", total_goals)
print("Total Assists:", total_assists)


df['Goal-to-Assist Ratio'] = df['Goals'] / df['Assists']
print("\nGoal-to-Assist Ratio per Season:")
print(df[['Season', 'Goal-to-Assist Ratio']])
