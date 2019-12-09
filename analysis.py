import matplotlib.pyplot as plt
import csv
import sys
import pandas as pd

inputsize = []
runtime = []
lang = []

with open(sys.argv[1],'r') as csvfile:
  plots = csv.reader(csvfile, delimiter=',')
  for row in plots:
    inputsize.append(int(row[1]))
    runtime.append(int(row[2]))
    labels.append(str(row[0]))

df = pd.DataFrame(dict(x=inputsize, y=runtime, label=lang))
langs = df.groupby('lang')

fig, ax = plt.subplots()
ax.margins(0.05) # Optional, just adds 5% padding to the autoscaling
for name, lang in langs:
    ax.plot(group.x, group.y, marker='o', linestyle='', ms=12, label=name)
ax.legend()