import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
from scipy import stats

df = pd.read_csv(
    r"C:\Users\jorda\Desktop\complete-data\name_msg_desc_like_reacts_min_5\name_msg_desc_links_like_reacts_min_100.csv")
# df = df.sample(frac=1).reset_index(drop=True)
df = df.iloc[:20000]

df = df.drop('message', 1)
df = df.drop('description', 1)
df = df.drop('likes_count', 1)
df = df[df['name'].apply(lambda x: isinstance(x, str))]

df_reacts = df.select_dtypes(include=[np.number])

df_reacts = df_reacts.div(df_reacts.sum(axis=1), axis=0)
df[df_reacts.columns] = df_reacts


analyser = SentimentIntensityAnalyzer()
scores = []

for index, row in df.iterrows():
    # print(row)
    score = analyser.polarity_scores(row['name'])
    scores.append(score['compound'])

    # blob = TextBlob(row['name'])
    # score = blob.sentiment.polarity
    # scores.append(score)

df['sen_score'] = scores

df = df[abs(df['sen_score']) != 0]
curr_react = 'wow_count'
df = df[abs(df[curr_react]) != 1]

# print(df)

# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binned_statistic.html
bin_means, bin_edges, binnumber = stats.binned_statistic(df[curr_react], df['sen_score'], statistic='mean', bins=np.arange(0, 1.1, 0.05).tolist()
                                                         )
fig = plt.figure()
fig.suptitle('Sentiment Score vs Wow Ratio', fontsize=14)
plt.hlines(bin_means, bin_edges[:-1], bin_edges[1:],
           colors='royalblue', lw=5, label='avg. sentiment for range', zorder=2)
plt.plot(df[curr_react], df['sen_score'], 'x',
         label='headline', zorder=1, color="grey")
plt.xlabel('Wow Ratio', fontsize=12)
plt.ylabel('Sentiment Score', fontsize=12)
plt.legend()
plt.savefig('wow_20k_min_100.png', bbox_inches='tight')
