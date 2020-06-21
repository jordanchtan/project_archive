import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

reacts = ['Love', 'Wow', 'Haha', 'Sad', 'Angry']

df = pd.read_csv(
    r"C:\Users\jorda\Desktop\EvaluationData\ReactData\7_No_Likes_min_20.csv", encoding='utf16')

df = df.iloc[:1000]

swarm_df = pd.DataFrame(columns=['reaction', 'ratio'])


for r in reacts:
    new_df = pd.DataFrame()
    col = '%s_count' % r.lower()
    new_df['ratio'] = df[col]
    new_df['reaction'] = r
    swarm_df = pd.concat([swarm_df, new_df])

print(swarm_df.head())
plt.figure()

# strip violin box swarm
ax = sns.stripplot(y="reaction", x="ratio", data=swarm_df, alpha=0.1)
plt.savefig('./Facebook/swarm_reacts')
