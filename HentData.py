import pandas as pd 
import requests
r = requests.get("https://covid.ourworldindata.org/data/owid-covid-data.csv", allow_redirects=True)
open("corona_data.csv", 'wb').write(r.content)
#"""https://opendata.ecdc.europa.eu/covid19/casedistribution/csv"""
corona_data = pd.read_csv("corona_data.csv",sep= ',')

print(corona_data)
#data = corona_data[corona_data["countriesAndTerritories"]=="Afghanistan"]

#print(data)
#death = 0
#for counter in range(len(data)):
#    death += data["deaths"][counter]
#print(death)
