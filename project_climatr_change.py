import pandas as pd
import numpy as np
import scipy.stats as sct
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

print("REALLY?")
# news

print("interesting")

print("now even more interesting")
print("how this is possble?")

print("now in main")

print("where it is?")

gt = pd.read_csv('GHCND_sample_csv.csv')

gt.describe
print("k")

print("done?")

df = pd.read_csv(r'C:\Users\Behzod\Documents\python\python tutorials_QY\python project climate\Climet_proj_pyth_vis-1\Environment_Temperature_change_E_All_Data_Normalized.csv', encoding="latin1")
print(df)

df.dtypes

df.describe()
print('d')

df[['Area', 'Value']].groupby(['Area']).mean().sort_values('Value')
plt.figure(figsize=(9, 4))
sns.lineplot(x="Year", y="Value", data=df)
plt.show()
df.head()
fig2 = px.scatter(df, x="Year", y="Value", color="Area")
fig2.show()


fig3 = px.line(df[df["Area"] == "Uzbekistan"], x="Year", y="Value")
fig3.show()


fig = px.choropleth(df, locations="Area",
                    locationmode='country names', color="Value",
                    hover_name="Area", range_color=[1, 1000],
                    color_continuous_scale="blues",
                    title="Climate change in 2020")
fig.update(layout_coloraxis_showscale=True)
fig.show()
