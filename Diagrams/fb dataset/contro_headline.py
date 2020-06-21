
# BREAKING: Hillary Clinton has won the South Carolina Democratic primary, CNN projects. Complete coverage online: cnn.it/SCPrimary and cnn.it/go
# likes 20876
# love 1718
# wow 153
# haha 116
# sad 239
# angry 1718
# 2016-02-28T00:00:34

import matplotlib.pyplot as plt

import seaborn as sns
import pandas as pd
sns.set(style="darkgrid")
d = {'Reaction': ['Love', 'Wow', 'Haha', 'Sad',
                  'Angry'], 'Count': [1718, 153, 116, 239, 1718]}
df = pd.DataFrame(data=d)

# ax = sns.countplot(x="Category", data=df)
ax = sns.barplot(x="Reaction", y="Count", data=df)
ax.set_title(
    '"Hillary Clinton has won the South Carolina Democratic primary"')
plt.savefig('./Facebook/contro_headline')
