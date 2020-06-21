import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

reacts = ['Love', 'Wow', 'Haha', 'Sad', 'Angry']

df = pd.read_csv(
    r"C:\Users\jorda\Desktop\EvaluationData\ReactDataCounts\2_No_Likes.csv", encoding='utf16')

df = df.sort_values('haha_count', ascending=False)
df = df[-9:-8]
print(df['haha_count'].values)
print(df['love_count'].values)
print(df['wow_count'].values)
print(df['sad_count'].values)
print(df['angry_count'].values)
print(df['name'].values)
