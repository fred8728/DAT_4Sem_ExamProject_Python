import numpy as np 
import pandas as pd 
import requests
r = requests.get("https://opendata.ecdc.europa.eu/covid19/casedistribution/csv", allow_redirects=True)
open("corona_data.csv", 'wb').write(r.content)

balance_data = pd.read_csv("corona_data.csv",sep= ',')

print(balance_data)
#print(balance_data["Afghanistan"])
#balance_data["Afghanistan"]