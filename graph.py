import pandas as pd
import glob, os, json
import matplotlib.pyplot as plt
import mpld3

df = pd.DataFrame()
path_to_json = 'json/'
json_pattern = os.path.join(path_to_json, '*.json')
file_list = glob.glob(json_pattern)

for file in file_list:
    data = pd.read_json(file, lines=True)
    df = df.append(data)

ax = df.plot(x='date', y='total',title ='Covid-19 Cases in California', kind = 'line')
ax.set_xlabel("Time")
ax.set_ylabel("Cases")


fig = ax.get_figure()

html_str = mpld3.fig_to_html(fig)
html_file = open("index.html","w")
html_file.write(html_str)
html_file.close()
