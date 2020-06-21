import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
sns.set(font_scale=2)

cols = ['name', 'love_count', 'wow_count',
        'haha_count', 'sad_count', 'angry_count']

df = pd.read_csv(
    # r"C:\Users\jorda\Desktop\EvaluationData\ReactData\5_No_Likes_min_10.csv", encoding='utf16', usecols=cols)
    r"C:\Users\jorda\Desktop\EvaluationData\ReactData\8_No_Likes_min_100.csv", encoding='utf16', usecols=cols)
df = df.sample(frac=1).reset_index(drop=True)
# df = df.iloc[:20000]

# df = df[df['name'].apply(lambda x: isinstance(x, str))]

# analyser = SentimentIntensityAnalyzer()
# scores = []
# for index, row in df.iterrows():
#     score = analyser.polarity_scores(row['name'])
#     scores.append(score['compound'])

# df['sen_score'] = scores

print(df.head())


def correlation_heatmap(df):
    correlations = df.corr(method='spearman')
    labels = ['Love', 'Wow', 'Haha', 'Sad', 'Angry']
    fig, ax = plt.subplots(figsize=(10, 10))
    sns.heatmap(correlations, fmt='.2f', vmax=1.0,
                square=True, annot=True, cbar_kws={"shrink": .70}, xticklabels=labels, yticklabels=labels, annot_kws={"fontsize": 18})

    plt.savefig('./original/cat_cat_heatmap/cat_cat_heatmap_min_100.png',
                bbox_inches='tight')
    plt.show()


correlation_heatmap(df)
