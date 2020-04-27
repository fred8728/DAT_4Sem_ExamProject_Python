import numpy as np 
import pandas as pd 
import requests
r = requests.get("https://opendata.ecdc.europa.eu/covid19/casedistribution/csv", allow_redirects=True)
open("corona_data.csv", 'wb').write(r.content)

corona_data = pd.read_csv("corona_data.csv",sep= ',')

print(corona_data)
data = corona_data[corona_data["countriesAndTerritories"]=="Afghanistan"]

print(data)
death = 0
for counter in range(len(data)):
    death += data["deaths"][counter]
print(death)
