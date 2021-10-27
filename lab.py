import csv
from matplotlib import pyplot as plt

"""
Compare mean scale score Asians, Blacks, and Hispanics in grades 3-8 in 2006
"""

filename = "Math.csv"
rows = []

with open(filename, 'r') as csvfile:

    csvreader = csv.reader(csvfile)
    fields = next(csvreader)

    for row in csvreader:
        rows.append(row)

asianMean = []
blackMean = []
hispanicMean = []

grades = ['3', '4', '5', '6', '7', '8']

grade = 0
year = 1
category = 2
meanScaleScore = 4

for row in rows:
    if row[grade] in grades and row[year] == '2006':
        if row[category] == "Asian":
            asianMean += [row[meanScaleScore]]
        elif row[category] == "Black":
            blackMean += [row[meanScaleScore]]
        elif row[category] == "Hispanic":
            hispanicMean += [row[meanScaleScore]]


plt.xlabel('Year')
plt.ylabel('Mean Scale Score')
plt.title('Category vs. Mean Scale Score (2006)')
plt.plot(grades, asianMean, color = '#D9514EFF', marker = 'o' , linewidth = 3, label = 'Asian')
plt.plot(grades, hispanicMean, color = '#2A2B2DFF', marker = 'o', linewidth = 3, label = 'Hispanic')
plt.tight_layout()
minY = min(min(asianMean), min(hispanicMean))
maxY = max(max(asianMean), max(hispanicMean))
plt.ylim('615', '700')
plt.legend()
plt.grid()
plt.savefig('meanScaleScore.jpg')

plt.show()