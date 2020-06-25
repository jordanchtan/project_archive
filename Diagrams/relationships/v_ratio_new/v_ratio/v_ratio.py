from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="ticks", color_codes=True)
sns.set(font_scale=1.4)

is_lowess = True
cols = ['name', 'love_count', 'wow_count',
        'haha_count', 'sad_count', 'angry_count']

df = pd.read_csv(
    r"C:\Users\jorda\Desktop\EvaluationData\ReactData\8_No_Likes_min_100.csv", encoding='utf16', usecols=cols)
# r"C:\Users\jorda\Desktop\EvaluationData\ReactData\2_No_Likes.csv", encoding='utf16', usecols=cols)
df = df.sample(frac=1).reset_index(drop=True)
df = df.iloc[:10000]


df = df[df['name'].apply(lambda x: isinstance(x, str))]


analyser = SentimentIntensityAnalyzer()
scores = []
for index, row in df.iterrows():
    score = analyser.polarity_scores(row['name'])
    scores.append(score['compound'])

df['sen_score'] = scores

df = df[abs(df['sen_score']) != 0]

for curr_react_name in ['Love', 'Haha', 'Wow', 'Angry', 'Sad']:
    print(curr_react_name)
    plt.figure()
    curr_react = curr_react_name.lower() + '_count'

    # df = df[abs(df[curr_react]) != 1]

    # ax = sns.regplot(x="sen_score", y=curr_react, data=df, x_bins=100
    #                  alpha=1, color='lightblue', n_boot='100')
    ax = sns.regplot(x="sen_score", y=curr_react, data=df, x_bins=100, ci=95,
                     lowess=is_lowess, line_kws={'color': 'red'}, scatter_kws={"s": 10, 'alpha': 0.15, 'color': 'lightblue'})

    ax.set(xlabel='Writer Valence Score',
           ylabel='Reader ' + curr_react_name + ' Ratio')

    path = './v_ratio_new/v_ratio_' + curr_react_name.lower()
    if is_lowess:
        path = path + '_lowess'
    path = path + '.png'
    plt.savefig(path, bbox_inches='tight')
