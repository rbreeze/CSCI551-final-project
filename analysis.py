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
    inputsize.append(float(row[1]))
    runtime.append(float(row[2]))
    lang.append(str(row[0]))

df = pd.DataFrame(dict(x=inputsize, y=runtime, label=lang))
langs = df.groupby('label')

with plt.xkcd():
  fig, ax = plt.subplots()
  ax.set_title(sys.argv[1].replace(".csv", "").upper())
  ax.set_xscale('log')
  ax.set_yscale('log')
  ax.set_xlabel('Input Size')
  ax.set_ylabel('Run Time (sec)')
  ax.margins(0.05) # Optional, just adds 5% padding to the autoscaling
  for name, lang in langs:
    ax.plot(lang.x, lang.y, marker='o', linestyle='', ms=6, alpha=0.7, label=name)
  ax.legend()
  plt.show()