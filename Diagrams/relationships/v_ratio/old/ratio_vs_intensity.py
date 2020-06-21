import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

df = pd.read_csv(
    r"C:\Users\jorda\Desktop\complete-data\name_msg_desc_like_reacts_min_5\name_msg_desc_links_like_reacts_min_100.csv")
# df = df.sample(frac=1).reset_index(drop=True)
df = df.iloc[:1000]

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


print(df)

# Prepare Data
# Create as many colors as there are unique midwest['category']

love_group = (df['love_count'].to_numpy(), df['sen_score'].to_numpy())
haha_group = (df['haha_count'].to_numpy(), df['sen_score'].to_numpy())
sad_group = (df['sad_count'].to_numpy(), df['sen_score'].to_numpy())
wow_group = (df['wow_count'].to_numpy(), df['sen_score'].to_numpy())
angry_group = (df['angry_count'].to_numpy(), df['sen_score'].to_numpy())

data = [love_group]
# data = (love_group, haha_group, sad_group, wow_group, angry_group)
colors = ["red"]
groups = ["love"]

# colors = ("red", "green", "blue", "pink", "black")
# groups = ("love", "haha", "sad", "wow", "angry")

# Create plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, facecolor="1.0")

for data, color, group in zip(data, colors, groups):
    x, y = data
    ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=30, label=group)

plt.title('Matplot scatter plot')
plt.legend(loc=2)
plt.show()
