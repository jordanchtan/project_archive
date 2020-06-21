import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
reacts = ['Love', 'Wow', 'Haha', 'Sad', 'Angry']

# df = pd.read_csv(
#     r"C:\Users\jorda\Desktop\FB-Data\all_combined.csv", encoding='utf16')
df = pd.read_csv(
    r"C:\Users\jorda\Desktop\EvaluationData\ReactDataCounts\2_No_Likes.csv", encoding='utf16')

df['react_sum'] = df['love_count'] + df['wow_count'] + \
    df['sad_count'] + df['haha_count'] + df['angry_count']
summ = sum(df['react_sum'].values)
print(summ)
