from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="ticks", color_codes=True)

is_lowess = True
cols = ['name', 'love_count', 'wow_count',
        'haha_count', 'sad_count', 'angry_count']

df = pd.read_csv(
    r"C:\Users\jorda\Desktop\EvaluationData\ReactData\5_No_Likes_min_10.csv", encoding='utf16', usecols=cols)
# r"C:\Users\jorda\Desktop\EvaluationData\ReactData\5_No_Likes_min_10.csv", encoding='utf16', usecols=cols)
# r"C:\Users\jorda\Desktop\EvaluationData\ReactData\2_No_Likes.csv", encoding='utf16', usecols=cols)
# df = df.sample(frac=1).reset_index(drop=True)
df = df.iloc[:10000]

# names = ['Love', 'Sad', 'Angry']
names = ['Wow', 'Love', 'Haha', 'Angry', 'Sad']
for i, curr_react_name in enumerate(names):
    for j, curr_react_name_2 in enumerate(names):
        if i == j:
            continue
        print(curr_react_name, curr_react_name_2)
        plt.figure()
        curr_react = curr_react_name.lower() + '_count'
        curr_react_2 = curr_react_name_2.lower() + '_count'

        # df = df[abs(df[curr_react]) != 1]

        ax = sns.regplot(x=curr_react, y=curr_react_2, data=df,
                         lowess=is_lowess, x_bins=100, ci=95, line_kws={'color': 'red'}, scatter_kws={"s": 10, 'alpha': 0.15, 'color': 'lightblue'})
        ax.set(xlabel='Reader ' + curr_react_name + ' Ratio',
               ylabel='Reader ' + curr_react_name_2 + ' Ratio')

        path = './original/cat_cat/' + curr_react_name.lower() + '_' + \
            curr_react_name_2.lower()
        if is_lowess:
            path = path + '_lowess'
        path = path + '.png'
        plt.savefig(path, bbox_inches='tight')
