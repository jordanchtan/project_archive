import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set(font_scale=2)

cols_w = ['V_writer', 'A_writer', 'D_writer']
cols_r = ['V_reader', 'A_reader', 'D_reader']
cols_wr = cols_w + cols_r


def correlation_heatmap(df, curr):
    correlations = df.corr(method='spearman')
    if curr == 'wr':
        print(correlations)
        correlations = correlations[cols_w]
        correlations = correlations.loc[cols_r]
        print(correlations)

    fig, ax = plt.subplots(figsize=(10, 10))
    sns.heatmap(correlations, fmt='.2f',
                square=True, annot=True, cbar_kws={"shrink": .70}, annot_kws={"fontsize": 18})
    folder = './original/vad_vad_heatmap/'
    plt.savefig(folder+'vad_vad_heatmap_' + curr + '.png', bbox_inches='tight')


for cols in [cols_w, cols_r, cols_wr]:
    df = pd.read_csv(
        "./EmoBank_Writer_Reader_All/EmoBank_Writer_Reader_All.csv", usecols=cols)

    if cols == cols_w:
        curr = 'w'
    if cols == cols_r:
        curr = 'r'
    if cols == cols_wr:
        curr = 'wr'
    correlation_heatmap(df, curr)
