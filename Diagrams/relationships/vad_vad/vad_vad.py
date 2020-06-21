import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set(style="ticks", color_codes=True)
sns.set(font_scale=2)


cols_writer = ['V_writer', 'A_writer', 'D_writer']
cols_reader = ['V_reader', 'A_reader', 'D_reader']
cols_sd = ['stdV_writer', 'stdA_writer', 'stdD_writer',
           'stdV_reader', 'stdA_reader', 'stdD_reader']
cols_n = ['N_writer', 'N_reader']
cols = cols_writer + cols_reader
df = pd.read_csv(
    "./EmoBank_Writer_Reader_All/EmoBank_Writer_Reader_All.csv", usecols=cols)
# df = df.iloc[:1000]

# conditions
# min_n = 3
# print(len(df.index))
# df = df[df['N_writer'] > min_n]
# df = df[df['N_reader'] > min_n]
# print(len(df.index))

# ###
# g = sns.PairGrid(df)
# g = g.map_diag(plt.hist, edgecolor="w")
# g = g.map_offdiag(sns.regplot, x_bins=100, ci=95, lowess=True, scatter_kws={"s": 5,
#                                                                             'alpha': 0.15}, line_kws={'color': 'red'})

# plt.savefig('./original/vad_vad/new/vad_vad_all_lowess.png',
# bbox_inches = 'tight')

###
g2 = sns.PairGrid(df, x_vars=cols_writer, y_vars=cols_writer)
g2 = g2.map_diag(plt.hist, edgecolor="w")
g2 = g2.map_offdiag(sns.regplot, x_bins=100, ci=95, lowess=True, scatter_kws={"s": 5,
                                                                              'alpha': 0.15}, line_kws={'color': 'red'})

plt.savefig('./original/vad_vad/new/vad_vad_w_lowess.png',
            bbox_inches='tight')
# ###
g2 = sns.PairGrid(df, x_vars=cols_reader, y_vars=cols_reader)
g2 = g2.map_diag(plt.hist, edgecolor="w")
g2 = g2.map_offdiag(sns.regplot, x_bins=100, ci=95, lowess=True, scatter_kws={"s": 5,
                                                                              'alpha': 0.15}, line_kws={'color': 'red'})

plt.savefig('./original/vad_vad/new/vad_vad_r_lowess.png',
            bbox_inches='tight')

g2 = sns.PairGrid(df, x_vars=cols_writer, y_vars=cols_reader)
# g2 = g2.map_diag(plt.hist, edgecolor="w")
g2 = g2.map(sns.regplot, x_bins=100, ci=95, lowess=True, scatter_kws={"s": 5,
                                                                      'alpha': 0.15}, line_kws={'color': 'red'})

plt.savefig('./original/vad_vad/new/vad_vad_wr_lowess.png',
            bbox_inches='tight')

g2 = sns.PairGrid(df, x_vars=cols_reader, y_vars=cols_writer)
# g2 = g2.map_diag(plt.hist, edgecolor="w")
g2 = g2.map(sns.regplot, x_bins=100, ci=95, lowess=True, scatter_kws={"s": 5,
                                                                      'alpha': 0.15}, line_kws={'color': 'red'})

plt.savefig('./original/vad_vad/new/vad_vad_rw_lowess.png',
            bbox_inches='tight')


# # ###
# g3 = sns.PairGrid(df)
# g3 = g3.map_diag(plt.hist, edgecolor="w")
# g3 = g3.map_offdiag(sns.regplot, x_bins=100, ci=95, scatter_kws={"s": 5,
#                                                                  'alpha': 0.15}, line_kws={'color': 'red'})

# plt.savefig('./original/vad_vad/new/vad_vad_all.png', bbox_inches='tight')
# # ###
# g4 = sns.PairGrid(df, x_vars=cols_writer, y_vars=cols_reader)
# # g4 = g4.map_diag(plt.hist, edgecolor="w")
# g4 = g4.map(sns.regplot, x_bins=100, ci=95, scatter_kws={"s": 5,
#                                                          'alpha': 0.15}, line_kws={'color': 'red'})

# plt.savefig('./original/vad_vad/new/vad_vad_rw.png', bbox_inches='tight')
