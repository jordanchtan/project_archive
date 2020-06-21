import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="ticks", color_codes=True)
sns.set(font_scale=2)

cols_writer = ['v', 'a', 'd']
cols_reader = ['love', 'wow', 'haha', 'sad', 'angry']

sentences_holdout = np.load(
    "./original/vad_ratio_data/sentences_holdout.npy", allow_pickle=True)
labels_holdout = np.load(
    "./original/vad_ratio_data/labels_holdout.npy", allow_pickle=True)
express_predictions = np.load(
    "./original/vad_ratio_data/express_predictions.npy", allow_pickle=True)

name = sentences_holdout
love, wow, haha, sad, angry = np.hsplit(
    labels_holdout, 5)
love = love.flatten()
wow = wow.flatten()
haha = haha.flatten()
sad = sad.flatten()
angry = angry.flatten()

express_predictions = np.vstack(express_predictions)
v, a, d = np.hsplit(express_predictions, 3)
v = v.flatten()
a = a.flatten()
d = d.flatten()


df = pd.DataFrame({'name': name, 'love': love, 'wow': wow,
                   'haha': haha, 'sad': sad, 'angry': angry, 'v': v, 'a': a, 'd': d})

df = df.iloc[:20000]

# g2 = sns.PairGrid(df, x_vars=cols_writer, y_vars=cols_reader)
# g2 = g2.map(sns.regplot, lowess=True, scatter_kws={"s": 5,
#                                                    'alpha': 0.15}, line_kws={'color': 'red'})

# plt.savefig('./vad_ratio/vad_ratio_rw_lowess.png', bbox_inches='tight')


def correlation_heatmap(df):
    correlations = df.corr(method='spearman')
    vad_cols = ['v', 'a', 'd']
    react_cols = ['love', 'wow', 'haha', 'sad', 'angry']
    correlations = correlations.drop(vad_cols, axis=0)
    correlations = correlations.drop(react_cols, axis=1)

    fig, ax = plt.subplots(figsize=(10, 10))

    vad_cols = ['V', 'A', 'D']
    react_cols = ['Love', 'Wow', 'Haha', 'Sad', 'Angry']
    sns.heatmap(correlations, fmt='.2f', vmax=1.0,
                square=True, annot=True, cbar_kws={"shrink": .70}, xticklabels=vad_cols, yticklabels=react_cols, annot_kws={"fontsize": 18})

    plt.savefig('./original/vad_ratio_heatmap/vad_ratio_heatmap.png',
                bbox_inches='tight')
    plt.show()


correlation_heatmap(df)
