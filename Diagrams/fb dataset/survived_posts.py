import matplotlib.pyplot as plt

import seaborn as sns
import pandas as pd
sns.set(style="darkgrid", font_scale=1.1)
d = {'Filter': ['All', 'Only Links', 'Links + Min 1 Reaction'],
     'Count': [534391, 427480, 155746]}
df = pd.DataFrame(data=d)

# ax = sns.countplot(x="Category", data=df)
ax = sns.barplot(x="Filter", y="Count", data=df)
ax.set_title(
    'Survived Posts')
plt.savefig('./Facebook/survived_posts', bbox_inches="tight")
