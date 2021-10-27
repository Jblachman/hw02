import csv
from matplotlib import pyplot as plt

"""
Compare mean scale score Asians, Blacks, and Hispanics in grades 3-8 in 2006
"""

filename = "Murder.csv"
rows = []

with open(filename, 'r') as csvfile:

    csvreader = csv.reader(csvfile)
    fields = next(csvreader)

    for row in csvreader:
        rows.append(row)

indicatorVal2005 = 0
indicatorVal2006 = 0
indicatorVal2007 = 0

year = 2
indicatorValue = 5

for row in rows:
    if row[year] == '2005':
        if row[indicatorValue]:
            indicatorVal2005 += int(row[indicatorValue])
    elif row[year] == '2006':
        if row[indicatorValue]:
            indicatorVal2006 += int(row[indicatorValue])
    elif row[year] == '2007':
        if row[indicatorValue]:
            indicatorVal2007 += int(row[indicatorValue])



barData = [indicatorVal2005, indicatorVal2006, indicatorVal2007]
labels = ["2005", "2006", "2007"]
explode = [0,0.1,0]
colors = ['#A9F3FD','#02AFC5','#FAFD7CFF']

plt.pie(barData, labels = labels, colors=colors, explode=explode, shadow = True, startangle=90, autopct="%1.1f%%", wedgeprops={'edgecolor': 'black'})

plt.title("Total indicator value of 2005, 2006, and 2007")
plt.savefig('indicatorValue.jpg')
plt.show()