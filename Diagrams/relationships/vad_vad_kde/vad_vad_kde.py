import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set(style="ticks", color_codes=True)


cols_writer = ['V_writer', 'A_writer', 'D_writer']
cols_reader = ['V_reader', 'A_reader', 'D_reader']
cols_sd = ['stdV_writer', 'stdA_writer', 'stdD_writer',
           'stdV_reader', 'stdA_reader', 'stdD_reader']
cols_n = ['N_writer', 'N_reader']
cols = cols_writer + cols_reader
df = pd.read_csv(
    "./EmoBank_Writer_Reader_All/EmoBank_Writer_Reader_All.csv", usecols=cols)
# df = df.iloc[:10000]

# conditions
# min_n = 3
# print(len(df.index))
# df = df[df['N_writer'] > min_n]
# df = df[df['N_reader'] > min_n]
# print(len(df.index))

# ###
# g = sns.PairGrid(df)
# g = g.map_diag(plt.hist, edgecolor="w")
# g = g.map_offdiag(sns.regplot, lowess=True, scatter_kws={"s": 5,
#                                                          'alpha': 0.15}, line_kws={'color': 'red'})

# plt.savefig('./vad_vad/vad_vad_all_lowess.png', bbox_inches='tight')
# ###
# g2 = sns.PairGrid(df, x_vars=cols_writer, y_vars=cols_reader)
# # g2 = g2.map_diag(plt.hist, edgecolor="w")
# g2 = g2.map(sns.regplot, lowess=True, scatter_kws={"s": 5,
#                                                    'alpha': 0.15}, line_kws={'color': 'red'})

# plt.savefig('./vad_vad/vad_vad_rw_lowess.png', bbox_inches='tight')
###
x = df['V_reader'].values
y = df['D_reader'].values
print(x[:10])
# ax = sns.kdeplot(x, y, shade=True)
# ax = sns.jointplot(x='V_reader', y='D_reader', data=df, kind="kde")
f, ax = plt.subplots(figsize=(6, 6))
sns.kdeplot(x, y, ax=ax)
# sns.rugplot(x, color="g", ax=ax)
# sns.rugplot(y, vertical=True, ax=ax)

plt.savefig('./original/vad_vad_kde/vad_vad_kde_w_lowess.png',
            bbox_inches='tight')
###
# g2 = sns.PairGrid(df, x_vars=cols_reader, y_vars=cols_reader)
# g2 = g2.map_diag(plt.hist, edgecolor="w")
# g2 = g2.map_offdiag(sns.regplot, lowess=True, scatter_kws={"s": 5,
#                                                            'alpha': 0.15}, line_kws={'color': 'red'})
# ax = sns.kdeplot(df[cols_writer], df[cols_reader], shade=True)
# plt.savefig('./original/vad_vad_kde/vad_vad_kde_r_lowess.png',
#             bbox_inches='tight')


# ###
# g3 = sns.PairGrid(df)
# g3 = g3.map_diag(plt.hist, edgecolor="w")
# g3 = g3.map_offdiag(sns.regplot, scatter_kws={"s": 5,
#                                               'alpha': 0.15}, line_kws={'color': 'red'})

# plt.savefig('./vad_vad/vad_vad_all.png', bbox_inches='tight')
# ###
# g4 = sns.PairGrid(df, x_vars=cols_writer, y_vars=cols_reader)
# # g4 = g4.map_diag(plt.hist, edgecolor="w")
# g4 = g4.map(sns.regplot, scatter_kws={"s": 5,
#                                       'alpha': 0.15}, line_kws={'color': 'red'})

# plt.savefig('./vad_vad/vad_vad_rw.png', bbox_inches='tight')
