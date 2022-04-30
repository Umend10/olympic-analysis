import pandas as pd

event1=pd.read_csv("athlete_events.csv")
country=pd.read_csv("noc_regions.csv")

##For send summer data only then merge data with NOC
def transform(d1,d2):
    d1=d1.query("Season=='Summer'")
    d1=d1.drop_duplicates()
    d1=d1.merge(d2,on='NOC',how='left')
    medal_dum=pd.get_dummies(d1['Medal'])
    d1=pd.concat([d1,medal_dum],axis=1)
    return d1
    