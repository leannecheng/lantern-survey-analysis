# ============================================================================ #
#                       Lantern: Student Survey Data Analysis                  #
# ============================================================================ #
# Author: Leanne Cheng
# Description: Generates four visualizations to analyze the learning patterns of
# 71 high school Mandarin Chinese students from Chicago and Kansas City.
# ============================================================================ #

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read the data
df = pd.read_csv('LanternStudentData.csv')

# shorten column names
df.rename(columns={'I think that a podcast and media-based app like Lantern would deepen my understanding of the language I want to learn.' : 'Effectiveness'}, inplace=True)
df.rename(columns={'I would be interested in using a podcast and media-based app like Lantern to further my language learning.' : 'Interest'}, inplace=True)
df.rename(columns={'Which methods of self-studying a new language do you prefer?' : 'Self_Study'}, inplace=True)
df.rename(columns={'If you want to learn more about Chinese culture, what do you want to learn about?' : 'Learn_More'}, inplace=True)
df.rename(columns={'I want to learn more about Chinese culture!' : 'Want_Learn'}, inplace=True)

# create new dataframes based on keywords of interest
df_food = df[df['Learn_More'].str.contains("food", case=False)]
df_culture = df[df['Learn_More'].str.contains("culture", case=False)]
df_history = df[df['Learn_More'].str.contains("history", case=False)]
df_social = df[df['Learn_More'].str.contains("social", case=False)]
df_language = df[df['Learn_More'].str.contains("language", case=False)]
df_music = df[df['Learn_More'].str.contains("music", case=False)]

# create arrays of keywords and keyword instances
keyword = ["food", "culture", "history", "social", "language", "music"]
num_instances = [len(df_food), len(df_culture), len(df_history), len(df_social), len(df_language), len(df_music)]

# calculate correlation between effectiveness and interest
correlation = df['Effectiveness'].corr(df['Interest'])
print(f"Correlation between Effectiveness and Interest: {correlation}") 

# plot configuration
fig = plt.figure(figsize=(10, 8))
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)   
ax4 = fig.add_subplot(224)

# ---------------- Plot #1: Most Interesting Topics by Keyword ---------------- #

ax1.bar(keyword, num_instances, color="#f2a356", edgecolor='black')
ax1.set_title("Students' Most Interested Topics")
ax1.set_xlabel('Keyword')
ax1.set_ylabel('# of Students')

# ---------------- Plot #2: Preferred Self-Study Methods ---------------- #

# create new dataframes for each self-study category
df_tv = df[df['Self_Study'].str.contains("TV")]
df_txt = df[df['Self_Study'].str.contains("textbooks")]
df_speak = df[df['Self_Study'].str.contains("native")]
df_music = df[df['Self_Study'].str.contains("music")]

# create arrays for plot 2
study_categories = ['Reading Textbooks', 'Watching Media', 'Speaking', 'Listening to Music']
num_self_study = [len(df_txt), len(df_tv), len(df_speak), len(df_music)]

ax2.pie(num_self_study, autopct='%1.1f%%', wedgeprops={'edgecolor': 'black', 'linewidth': 1, 'linestyle': 'solid'}, colors=['#f27c70', '#f2a356', '#f0d056', '#e07b5a'])
ax2.set_title('Preferred Methods of Self-Study', fontsize=15)
ax2.legend(study_categories, title="Study Methods", loc="upper left", bbox_to_anchor=(0.9, 0.9), fontsize=7, title_fontsize=8)

# ---------------- Plot #3: Self-study Methods vs. Lantern Interest/Effectiveness ---------------- #

df_comprehension = df[df['Self_Study'].str.contains("Listening to music, Watching TV shows/movies, Talking to native speakers")]

# make a bunch of variables for mean interest
all_interest_mean = df['Interest'].mean()
CI_interest_mean = df_comprehension['Interest'].mean()
txt_interest_mean = df_txt['Interest'].mean()
tv_interest_mean = df_tv['Interest'].mean()
speak_interest_mean = df_speak['Interest'].mean()
music_interest_mean = df_music['Interest'].mean()

# make a bunch of variables for mean effectiveness
all_eff_mean = df['Effectiveness'].mean()
CI_eff_mean = df_comprehension['Effectiveness'].mean()
txt_eff_mean = df_txt['Effectiveness'].mean()
tv_eff_mean = df_tv['Effectiveness'].mean()
speak_eff_mean = df_speak['Effectiveness'].mean()
music_eff_mean = df_music['Effectiveness'].mean()

# create arrays for plots
study_groups = ['Overall group', 'All CI', 'Textbook', 'Watching', 'Speaking', 'Listening']
interest_means = [all_interest_mean, CI_interest_mean, txt_interest_mean, tv_interest_mean, speak_interest_mean, music_interest_mean]
effectiveness_means = [all_eff_mean, CI_eff_mean, txt_eff_mean, tv_eff_mean, speak_eff_mean, music_eff_mean]

# double bar graph configuration
x_bar = np.arange(len(study_groups))
bar_width = 0.2
bars_interest = ax3.bar(x_bar - bar_width / 2, interest_means, bar_width, label='Interest', color='#e07b5a', edgecolor='black')
bars_eff = ax3.bar(x_bar + bar_width / 2, effectiveness_means, bar_width, label='Effectiveness', color='#f0d056', edgecolor='black')

ax3.set_xlabel('Preferred Method')
ax3.set_ylabel('Mean Rating (1-5)')
ax3.set_title('Study Methods vs. Lantern Interest/Effectiveness')
ax3.set_xticks(x_bar)
ax3.set_xticklabels(study_groups)
ax3.set_ylim(3.6, 4.4)
ax3.legend()

# ---------------- Plot #4: Lantern Interest Levels ---------------- #

# count number of students for each rating (1-5)
interest_counts = df['Interest'].value_counts()
effectiveness_counts = df['Effectiveness'].value_counts()

ax4.bar(interest_counts.index, interest_counts.values, color='#f0d056', edgecolor='black')

ax4.set_title('Lantern Interest Levels')
ax4.set_xlabel('Level of Interest (1-5)')
ax4.set_ylabel('# of Students')
ax4.set_xticks(range(0,6))

plt.tight_layout()
plt.show()
