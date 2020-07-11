import pandas as pd
import glob, os, json
import matplotlib.pyplot as plt
import mpld3

df = pd.DataFrame()
df1 = pd.DataFrame()
path_to_json = 'json/'
json_pattern = os.path.join(path_to_json, '*.json')
file_list = glob.glob(json_pattern)



for file in file_list:
    data = pd.read_json(file, lines=True)
    df = df.append({'date': data['date'], 'total': int(data['total'])}, ignore_index=True)
    df1['City'] = list(data['cities'][0])

    newList = data['cases']

newList = list(newList[0])

df1['Cases'] = newList

ax1 = df1.plot(x='City', y='Cases', kind = 'bar', figsize=(18,5), fontsize=8)
ax1.set_xlabel("City")
ax1.set_ylabel("Cases")
ax1.set_xticks(ax1.get_xticks()[::1])


ax = df.plot(x='date', y='total',title ='Covid-19 Cases in California', kind = 'line')
ax.set_xlabel("Time")
ax.set_ylabel("Cases")

fig = plt.figure(1)
fig2 = plt.figure(2)

#plt.show()


html_str = mpld3.fig_to_html(fig2)
html_file = open("index.html","w")
html_file.write(html_str)
html_str = mpld3.fig_to_html(fig)
html_file.write(html_str)
html_file.close()
