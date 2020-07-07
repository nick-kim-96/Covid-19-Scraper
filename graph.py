import pandas as pd
import glob, os, json
import matplotlib.pyplot as plt

df = pd.DataFrame()
path_to_json = 'json/'
json_pattern = os.path.join(path_to_json, '*.json')
file_list = glob.glob(json_pattern)

for file in file_list:
    data = pd.read_json(file, lines=True)
    df = df.append(data)

df.plot(x='date', y='total', kind = 'line')
plt.show()
