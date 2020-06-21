import matplotlib.pyplot as plt
import pandas as pd

# df = pd.read_csv(
#     r"C:\Users\jorda\Desktop\EvaluationData\ReactDataCounts\1_Likes.csv", encoding='utf16')
cols = ['name', 'likes_count', 'love_count', 'wow_count',
        'haha_count', 'sad_count', 'angry_count']

df = pd.read_csv(r"C:\Users\jorda\Desktop\FB-Data\name_msg_desc_links_like_reacts\name_msg_desc_links_like_reacts.csv",
                 usecols=cols, encoding='utf16')
df['react_sum'] = df['love_count'] + df['wow_count'] + \
    df['haha_count'] + df['sad_count'] + df['angry_count']

# df = df[df['react_sum'] > 0]

sums = [df['likes_count'].sum(), df['love_count'].sum(), df['wow_count'].sum(
), df['haha_count'].sum(), df['sad_count'].sum(), df['angry_count'].sum()]

percents = [s / sum(sums) * 100 for s in sums]

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
# labels = ['Like %1.1f%%' % percents[0], 'Love %1.1f%%' % percents[1], 'Wow %1.1f%%' % percents[2],
#           'Haha %1.1f%%' % percents[3], 'Sad %1.1f%%' % percents[4], 'Angry %1.1f%%' % percents[5]]

# fig1, ax1 = plt.subplots()

# patches, _ = ax1.pie(sums,                            startangle=90)
# plt.legend(patches, labels, loc="lower left")
# ax1.set_title("Total Count Percentage: Likes and Reactions")


# ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# plt.savefig('./Facebook/pie_all')

# quit()
#############################
labels = ['Like %1.1f%%' % percents[0], 'Love %1.1f%%' % percents[1], 'Wow %1.1f%%' % percents[2],
          'Haha %1.1f%%' % percents[3], 'Sad %1.1f%%' % percents[4], 'Angry %1.1f%%' % percents[5]]

fig1, ax1 = plt.subplots()

patches, _ = ax1.pie(sums,                            startangle=90)
plt.legend(patches, labels, loc="lower left")
ax1.set_title("Before FPercentages of Likes and Reactions")


ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.savefig('./Facebook/pie_all_no_min.png')

quit()
#############################

labels = ['Love', 'Wow', 'Haha', 'Sad', 'Angry']
sizes = sums[1:]
# explode = (0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        startangle=90)

ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax1.set_title("Total Count Percentage: Reactions Only")
plt.savefig('./Facebook/pie_reacts')
