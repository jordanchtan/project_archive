# from skmisc.loess import loess
import pylab as plt
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
    r"C:\Users\jorda\Desktop\EvaluationData\ReactData\8_No_Likes_min_100.csv", encoding='utf16', usecols=cols)
# r"C:\Users\jorda\Desktop\EvaluationData\ReactData\2_No_Likes.csv", encoding='utf16', usecols=cols)
df = df.sample(frac=1).reset_index(drop=True)
df = df.iloc[:20000]


df = df[df['name'].apply(lambda x: isinstance(x, str))]


analyser = SentimentIntensityAnalyzer()
scores = []
for index, row in df.iterrows():
    score = analyser.polarity_scores(row['name'])
    scores.append(score['compound'])

df['sen_score'] = scores

df = df[abs(df['sen_score']) != 0]

for curr_react_name in ['Wow', 'Love', 'Haha', 'Angry', 'Sad']:
    print(curr_react_name)
    plt.figure()
    curr_react = curr_react_name.lower() + '_count'

    # df = df[abs(df[curr_react]) != 1]

    ax = sns.regplot(x="sen_score", y=curr_react, data=df,
                     lowess=is_lowess, line_kws={'color': 'red'}, scatter_kws={"s": 10, 'alpha': 0.15, 'color': 'lightblue'})
    ax.set(xlabel='Writer Valence Score',
           ylabel='Reader ' + curr_react_name + ' Ratio')

    path = './v_ratio/v_ratio_' + curr_react_name.lower()
    if is_lowess:
        path = path + '_lowess'
    path = path + '.png'
    plt.savefig(path, bbox_inches='tight')


# x = df['love_count']
# y = df['sen_score']

# l = loess(x, y)
# l.fit()
# pred = l.predict(x, stderror=True)
# conf = pred.confidence()

# lowess = pred.values
# ll = conf.lower
# ul = conf.upper

# plt.plot(x, y, '+')
# plt.plot(x, lowess)
# plt.fill_between(x, ll, ul, alpha=.33)
# plt.show()
