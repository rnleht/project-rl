# Some of the code has been influenced by the example materials of the course. 

from os import listdir
import pandas as pd
import matplotlib.pyplot as plt
from statistics import mean
from scipy.stats import norm
from statsmodels.stats.anova import AnovaRM

dataPath = "Project_RL/data/"

fileList = listdir(dataPath)

columns = [
    "corrResp",
    "Response_1.keys",
    "Response_1.rt",
    "participant",
]

columns_2 = [
    "corrResp_2",
    "Response_2.keys",
    "Response_2.rt",
    "participant",
]

skipped_rows = [1, 2] + list(range(22, 43))
skipped_rows_2 = list(range(1, 22)) + [43]

df_from_each_file = (
    pd.read_csv(
        dataPath + f,
        usecols=columns,
        skiprows=skipped_rows
    ) for f in fileList if f.endswith(".csv"))

dataframes = pd.concat(df_from_each_file, ignore_index=True)

df_from_each_file_2 = (
    pd.read_csv(
        dataPath + f,
        usecols=columns_2,
        skiprows=skipped_rows_2
    ) for f in fileList if f.endswith(".csv"))

dataframes_2 = pd.concat(df_from_each_file_2, ignore_index=True)

corresp_RTs_1 = []
false_RTs_1 = []
corresp_RTs_2 = []
false_RTs_2 = []

for i, row in dataframes.iterrows():
    if row["corrResp"] == row["Response_1.keys"]:
        corresp_RTs_1.append(row["Response_1.rt"])

for i, row in dataframes.iterrows():
    if row["corrResp"] != row["Response_1.keys"]:
        false_RTs_1.append(row["Response_1.rt"])

for i, row in dataframes_2.iterrows():
    if row["corrResp_2"] == row["Response_2.keys"]:
        corresp_RTs_2.append(row["Response_2.rt"])

for i, row in dataframes_2.iterrows():
    if row["corrResp_2"] != row["Response_2.keys"]:
        false_RTs_2.append(row["Response_2.rt"])

false_RTs_1nonans = [x for x in false_RTs_1 if pd.isnull(x) == False and x != "nan"]
false_RTs_2nonans = [x for x in false_RTs_2 if pd.isnull(x) == False and x != "nan"]

correspRTmean_1 = mean(corresp_RTs_1)
falseRTmean_1 = mean(false_RTs_1nonans) 
correspRTmean_2 = mean(corresp_RTs_2)
falseRTmean_2 = mean(false_RTs_2nonans)

print (correspRTmean_1, falseRTmean_1, correspRTmean_2, falseRTmean_2)

fig, ax = plt.subplots()

bars = ax.bar([.5,1.5], [correspRTmean_1, correspRTmean_2], width=.4)
ax.set_ylabel('RT (s)')
ax.set_title('Mean Reaction Time (H)')
ax.set_xticks([.5,1.5])
ax.set_xticklabels(["One word", "Two words"])
plt.show()

bars = ax.bar([.5,1.5], [falseRTmean_1, falseRTmean_2], width=.4)
ax.set_ylabel('RT (s)')
ax.set_title('Mean Reaction Time (FA)')
ax.set_xticks([.5,1.5])
ax.set_xticklabels(["One word", "Two words"])
plt.show()

fig, ax = plt.subplots()
box = ax.boxplot([corresp_RTs_1, corresp_RTs_2])
ax.set_ylabel("RT (s)")
ax.set_title('Reaction Time (H)')
ax.set_xticklabels(["One Word", "Two words"])
plt.show()

fig, ax = plt.subplots()
box = ax.boxplot([false_RTs_1nonans, false_RTs_2nonans])
ax.set_ylabel("RT (s)")
ax.set_title('Reaction Time (FA)')
ax.set_xticklabels(["One Word", "Two words"])
plt.show()

accuracy = pd.DataFrame({"theCondition" : ["stimulusWord"],"hits" : [0], "misses" : [0], "CRs" : [0], "FAs" : [0]})

for index, row in dataframes.iterrows():
    rowInd = 0
    if row["corrResp"] == "left" and row["Response_1.keys"] == "left":
        accuracy.loc[rowInd,"hits"] += 1
    elif row["corrResp"] == "left" and row["Response_1.keys"] == "right":
        accuracy.loc[rowInd,"misses"] += 1
    elif row["corrResp"] == "right" and row["Response_1.keys"] == "right":
        accuracy.loc[rowInd,"CRs"] += 1
    elif row["corrResp"] == "right" and row["Response_1.keys"] == "left":
        accuracy.loc[rowInd,"FAs"] += 1

print(accuracy)

accuracy_2 = pd.DataFrame({"theCondition" : ["stimulusWord"],"hits" : [0], "misses" : [0], "CRs" : [0], "FAs" : [0]})

for index, row in dataframes_2.iterrows():
    rowInd = 0
    if row["corrResp_2"] == "left" and row["Response_2.keys"] == "left":
        accuracy_2.loc[rowInd,"hits"] += 1
    elif row["corrResp_2"] == "left" and row["Response_2.keys"] == "right":
        accuracy_2.loc[rowInd,"misses"] += 1
    elif row["corrResp_2"] == "right" and row["Response_2.keys"] == "right":
        accuracy_2.loc[rowInd,"CRs"] += 1
    elif row["corrResp_2"] == "right" and row["Response_2.keys"] == "left":
        accuracy_2.loc[rowInd,"FAs"] += 1

print(accuracy_2)

def dPrime(hitRate, FArate):
    stat = norm.ppf(hitRate) - norm.ppf(FArate)
    return stat
def criterion(hitRate, FArate):
    stat = -.5*(norm.ppf(hitRate) + norm.ppf(FArate))
    return stat

hitRateOneWord = accuracy.loc[0]["hits"]/80 
FArateOneWord = accuracy.loc[0]["FAs"]/80
hitRateTwoWords = accuracy_2.loc[0]["hits"]/80
FArateTwoWords = accuracy_2.loc[0]["FAs"]/80

print (dPrime(hitRateOneWord, FArateOneWord))
print (criterion(hitRateOneWord, FArateOneWord))

print (dPrime(hitRateTwoWords, FArateTwoWords))
print (criterion(hitRateTwoWords, FArateTwoWords))

#Here's what I was trying to do claculating the p-values

# counter = 0
# for dataFile in fileList:
#     counter += 1
#     pNum = "P-" + str(counter)

# meanRTsList = [mean(corresp_RTs_1), mean(corresp_RTs_2)]
# participant = [pNum, pNum]
# theAccuracy = [accuracy, accuracy_2]

# newLines = pd.DataFrame({"participant" : participant, "theAccuracy" : theAccuracy, "mean RT" : meanRTsList})
# model = AnovaRM(data = newLines, depvar = "mean RT", subject = "participant", within = ["theAccuracy"]).fit()

# print (model)