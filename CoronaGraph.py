import requests
import numpy as np
import matplotlib.pyplot as plt
import datetime
import json
import re

graphTitle = "Corona in Deutschland"
API = "https://api.covid19api.com/country/germany"
confirmedKey = "Confirmed"
deathKey = "Deaths"
dateKey = "Date"

x = requests.get(API)
arr = json.loads(x.text)
y = []
g = []
d = []
for x in arr:
    y.append(np.array(x[confirmedKey]))
    g.append(np.array(x[deathKey]))
    tmpdate = x[dateKey].split("T")[0].split("-")
    d.append(datetime.date(int(tmpdate[0]), int(tmpdate[1]), int(tmpdate[2])))

plt.plot(d, g, color="red", label="Tode")
plt.plot(d, y, color="orange", label="Infiziert")
plt.xticks(rotation=45, ha='right')
plt.legend(loc='best')
plt.title(graphTitle)
plt.xlabel('Zeit')
plt.ylabel('Menschen')
fig = plt.gcf()
fig.canvas.set_window_title(graphTitle)
fig.set_size_inches(11, 8)

plt.show()
