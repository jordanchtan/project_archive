import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

cols = ['name', 'love_count', 'wow_count',
        'haha_count', 'sad_count', 'angry_count']

df = pd.read_csv(
    r"C:\Users\jorda\Desktop\EvaluationData\ReactData\2_No_Likes.csv", encoding='utf16', usecols=cols)
# r"C:\Users\jorda\Desktop\EvaluationData\ReactData\8_No_Likes_min_100.csv", encoding='utf16', usecols=cols)
df = df.sample(frac=1).reset_index(drop=True)
df = df.iloc[:10000]

df = df[df['name'].apply(lambda x: isinstance(x, str))]

analyser = SentimentIntensityAnalyzer()
scores = []
for index, row in df.iterrows():
    score = analyser.polarity_scores(row['name'])
    scores.append(score['compound'])

df['sen_score'] = scores

print(df.head())


def correlation_heatmap(df):
    correlations = df.corr(method='spearman')
    vad_cols = ['sen_score']
    react_cols = ['love_count', 'wow_count',
                  'haha_count', 'sad_count', 'angry_count']
    correlations = correlations.drop(vad_cols, axis=1)
    correlations = correlations.drop(react_cols, axis=0)

    vad_cols = ['V']
    react_cols = ['Love', 'Wow', 'Haha', 'Sad', 'Angry']
    fig, ax = plt.subplots(figsize=(10, 10))
    sns.heatmap(correlations, fmt='.2f', vmax=1.0,
                square=True, annot=True, cbar_kws={"shrink": .70}, xticklabels=react_cols, yticklabels=vad_cols)

    plt.savefig('./original/v_ratio_heatmap/v_ratio_heatmap.png',
                bbox_inches='tight')
    plt.show()


correlation_heatmap(df)
