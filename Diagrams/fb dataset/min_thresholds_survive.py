import matplotlib.pyplot as plt

import seaborn as sns
import pandas as pd
sns.set(style="darkgrid", font_scale=1.1)
d = {'Min. Reactions': ['1', '5', '10', '15', '20', '25'],
     'Count': [155746, 122504, 112735, 106245, 101258, 97002]}
df = pd.DataFrame(data=d)

# ax = sns.countplot(x="Category", data=df)
ax = sns.barplot(x="Min. Reactions", y="Count", data=df, order=[
                 '1', '5', '10', '15', '20', '25'])
ax.set_title(
    'Survived Posts Across Minimum Reactions')
plt.savefig('./Facebook/min_threshold_survive', bbox_inches="tight")
