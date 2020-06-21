import matplotlib.pyplot as plt

import seaborn as sns
import pandas as pd
sns.set(style="darkgrid", font_scale=1.1)
d = {'Min. Reaction': ['1', '5', '10', '15', '20', '25'],
     'MSE': [0.0411, 0.0395, 0.0377, 0.0361, 0.0334,   0.0329]}
df = pd.DataFrame(data=d)

# ax = sns.countplot(x="Category", data=df)
ax = sns.barplot(x="Min. Reaction", y="MSE", data=df, order=[
                 '1', '5', '10', '15', '20', '25'])
ax.set_title(
    'Performance Across Min. Reactions')
plt.savefig('./Facebook/min_thresholds', bbox_inches="tight")
