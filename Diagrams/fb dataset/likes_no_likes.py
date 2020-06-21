import matplotlib.pyplot as plt

import seaborn as sns
import pandas as pd
sns.set(style="darkgrid", font_scale=1.1)
d = {'Include/Exclude Likes': ['Likes + Reacts', 'Reacts Only'],
     'MSE': [0.0063, 0.0518]}
df = pd.DataFrame(data=d)

# ax = sns.countplot(x="Category", data=df)
ax = sns.barplot(x="Include/Exclude Likes", y="MSE", data=df)
ax.set_title(
    'Performance: Including and Excluding Likes')
plt.savefig('./Facebook/likes_no_likes', bbox_inches="tight")
