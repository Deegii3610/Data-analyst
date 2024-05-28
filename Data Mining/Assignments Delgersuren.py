import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

csv_file_path = 'data_exploration.csv'
df = pd.read_csv(csv_file_path)
print(df.head())

dg = df[df['Survived'] == 1]
dp = df[df['Survived'] != 1]

fig, axs = plt.subplots(3, 3, figsize=(16, 16))

pie_bysurv = [len(dg), len(dp)]
axs[0, 0].pie(pie_bysurv, labels=["Survived", "Did not survived"], autopct='%1.1f%%')
axs[0, 0].set_title('By Survive')


woman = df['Sex'].value_counts()['female']
man = df['Sex'].value_counts()['male']

bysex = [woman, man]
axs[1, 0].pie(bysex, labels=["Woman", "Man"], autopct='%1.1f%%')
axs[1, 0].set_title('By Sex of all')

swoman = dg['Sex'].value_counts()['female']
sman = dg['Sex'].value_counts()['male']
axs[0, 1].pie([swoman, sman], labels=["Woman", "Man"], autopct='%1.1f%%')
axs[0, 1].set_title('By Sex of survived')

dwoman = dp['Sex'].value_counts()['female']
dman = dp['Sex'].value_counts()['male']
axs[0, 2].pie([dwoman, dman], labels=["Woman", "Man"], autopct='%1.1f%%')
axs[0, 2].set_title('By Sex of not survived')

clss1 = dg['Pclass'].value_counts()[1]
clss2 = dg['Pclass'].value_counts()[2]
clss3 = dg['Pclass'].value_counts()[3]
axs[1, 1].pie([clss1, clss2, clss3], labels=["Class 1", "Class 2", "Class 3"], autopct='%1.1f%%')
axs[1, 1].set_title('By Class of Survived')

dclss1 = dp['Pclass'].value_counts()[1]
dclss2 = dp['Pclass'].value_counts()[2]
dclss3 = dp['Pclass'].value_counts()[3]
axs[1, 2].pie([dclss1, dclss2, dclss3], labels=["Class 1", "Class 2", "Class 3"], autopct='%1.1f%%')
axs[1, 2].set_title('By Class of not Survived')

aclss1 = df['Pclass'].value_counts()[1]
aclss2 = df['Pclass'].value_counts()[2]
aclss3 = df['Pclass'].value_counts()[3]
axs[2, 0].pie([aclss1, aclss2, aclss3], labels=["Class 1", "Class 2", "Class 3"], autopct='%1.1f%%')
axs[2, 0].set_title('By Class of All')

ages = df["Age"].dropna()
axs[2, 1].hist(ages, bins=10, edgecolor="k", alpha=0.7)
axs[2, 1].set_xlabel("Age")
axs[2, 1].set_ylabel("Frequency")
axs[2, 1].set_title("Age Distribution of All")

sages = dg["Age"].dropna()
axs[2, 2].hist(sages, bins=10, edgecolor="b", alpha=1)
axs[2, 2].set_xlabel("Age")
axs[2, 2].set_ylabel("Frequency")
axs[2, 2].set_title("Age Distribution of Survived")


plt.show()

