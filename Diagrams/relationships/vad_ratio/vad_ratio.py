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
cols = ['love', 'wow', 'haha', 'sad', 'angry', 'v', 'a', 'd']
df = df.iloc[:10000]
# df[cols] = (df[cols]-df[cols].mean())/df[cols].std()

# g2 = sns.PairGrid(df, x_vars=cols_writer, y_vars=cols_reader)
# g2 = g2.map(sns.regplot, lowess=True, scatter_kws={"s": 5,
#                                                    'alpha': 0.15}, line_kws={'color': 'red'})

# plt.savefig('./vad_ratio/vad_ratio_rw_lowess.png', bbox_inches='tight')

is_lowess = True
for curr_react_name in ['Wow', 'Love', 'Haha', 'Angry', 'Sad']:
    for curr_express_name in ['V', 'A', 'D']:
        print(curr_react_name + ' ' + curr_express_name)
        plt.figure()
        curr_react = curr_react_name.lower()
        curr_express = curr_express_name.lower()

        # df = df[abs(df[curr_react]) != 1]

        ax = sns.regplot(x=curr_express, y=curr_react, data=df,
                         lowess=is_lowess, x_bins=100, ci=95, line_kws={'color': 'red'}, scatter_kws={"s": 10, 'alpha': 0.15, 'color': 'lightblue'})
        ax.set(ylim=(0, 1.0))
        # ax.set(xlim=(2, 4))

        ax.set(xlabel='Reader ' + curr_express_name + ' Score',
               ylabel='Reader ' + curr_react_name + ' Ratio')

        path = './original/vad_ratio/vad_ratio_' + curr_express_name.lower() + '_' + \
            curr_react_name.lower()
        if is_lowess:
            path = path + '_lowess'
        path = path + '.png'
        plt.savefig(path, bbox_inches='tight')
