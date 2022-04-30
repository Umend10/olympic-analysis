import numpy as np
def medal(d3):
    
    d3=d3.drop_duplicates(subset=['Team','NOC','Year','Sport','Event','Medal'])
    medal_list=d3.groupby('region').sum()[['Gold','Silver','Bronze']].sort_values('Gold',ascending=False).applymap(lambda x:np.int(x)).reset_index()
    medal_list['total']=medal_list['Gold']+medal_list["Silver"]+medal_list['Bronze']
    return medal_list

## country name and year name

def country_year_lsit(data):
    #year list
    year=data.Year.unique().tolist()
    year.sort()
    year.insert(0,'overall')

    #country list
    country=data.dropna(subset=['region'])
    country=country.region.unique().tolist()
    country.sort()
    country.insert(0,'overall')
    return year,country

##madel tally 
def medal_tally(data,year,country):

    flag=1
    data=data.drop_duplicates(subset=['Team','NOC','Year','Sport','Event','Medal'])
    if year=='overall' and country=='overall':
        data
    elif year=='overall' and country != 'overall':
        data=data[data.region==country]
    elif year!='overall' and country =='overall':
        data=data[data.Year==year]
    elif year!='overall' and country!='overall':
        data=data[(data.Year==year) & (data.region==country)]
        
    if flag==0:
        data=data.groupby('Year').sum()[['Gold',"Silver",'Bronze']].applymap(lambda x: np.int(x)).sort_values('Year',ascending=True).reset_index()
    else:
        data=data.groupby('region').sum()[['Gold',"Silver",'Bronze']].applymap(lambda x: np.int(x)).sort_values('Gold',ascending=False).reset_index()

    data['total']=data['Gold']+data["Silver"]+data["Bronze"]
    return data
##Line plo 
def graph(data,value):
    participation_by_year=data.drop_duplicates(['Year',value])['Year'].value_counts().reset_index().sort_values("index")
    participation_by_year.rename(columns={"index":'Year',"Year":value},inplace=True)
    return participation_by_year
##histmap 
def heatmap(event):
    event=event.drop_duplicates(['Year','Sport','Event'])[['Year','Sport','Event']]
    pivet_data=event.pivot_table(index="Sport",columns="Year",values="Event",aggfunc='count').fillna(0)
    return pivet_data

## Top 15 athletes

def athelit(data,select):
    data=data.dropna(subset=['Medal'])
    d=data.Name.value_counts().reset_index()
    d=d.merge(data,left_on='index',right_on='Name',how="left")[['index','region','Sport','Name_x']].drop_duplicates()
    if select=='overall':
        d=d.head(15)
        
    if select!='overall':
        d=d[d.Sport==select].head(15)
        
    return d.rename(columns={'index':'Name','Name_x':'Medal'})

##Sprot names
def Sport_name(data):
    name=data.Sport.unique().tolist()
    name.sort()
    name.insert(0,'overall')
    return name



#plot  for country wise analysis
def country_name_analysis(data,name):
    data=data[data.Medal!=np.nan]
    data=data.drop_duplicates(['Team','NOC','Year','Sport','Event','Medal'])
    data=data[data.region==name]
    data=data.groupby('Year').count()['Medal']
                             
    return data.reset_index()

#heatmap for counry wise medal

def medal_analysis_county_wise_hitmap(data,country):
    data=data[data.region==country]
    data_heat=data.drop_duplicates(['Team','NOC','Year','Sport','Event','Medal'])[['Year','Medal','Sport']]
    data_heat=data_heat.pivot_table(index="Sport",columns="Year",values="Medal",aggfunc='count').fillna(0)
    return data_heat

def athlete_by_country(data,country,select):
    data=data[data.region==country]
    data=data.dropna(subset=['Medal'])
    d=data.Name.value_counts().reset_index()
    d=d.merge(data,left_on='index',right_on='Name',how="left")[['index','Sport','Name_x']].drop_duplicates()
    if select=='overall':
        d=d.head(15)
        
    if select!='overall':
        d=d[d.Sport==select].head(15)
        
    return d.rename(columns={'index':'Name','Name_x':'Medal'})

#Age based medal winner and participation
def medal_dist_on_age(data,medal_type):
    
    if medal_type=='participate':
        data=data.drop_duplicates(['Name','Year',"Age"])
    if medal_type not in ['participate','overall']:
        data=data[data.Medal==medal_type]
    if medal_type=='overall':
        data=data[data.Medal.isin(['Gold','Silver','Bronze'])]    
    return data.Age
#weight wise medal analysis

def medal_dist_on_weight(data,medal_type):
    
    if medal_type=='participate':
        data=data.drop_duplicates(['Name','Year',"Age"])
    if medal_type not in ['participate','overall']:
        data=data[data.Medal==medal_type]
    if medal_type=='overall':
        data=data[data.Medal.isin(['Gold','Silver','Bronze'])]    
    return data.Weight

#height wise medal analysis

def medal_dist_on_height(data,medal_type):
    
    if medal_type=='participate':
        data=data.drop_duplicates(['Name','Year',"Age"])
    if medal_type not in ['participate','overall']:
        data=data[data.Medal==medal_type]
    if medal_type=='overall':
        data=data[data.Medal.isin(['Gold','Silver','Bronze'])]    
    return data.Height

#gender wise medal analysis

def medal_dist_on_gender(data,medal_type):
    
    if medal_type=='participate':
        data=data.drop_duplicates(['Name','Year',"Age"])
    if medal_type not in ['participate','overall']:
        data=data[data.Medal==medal_type]
    if medal_type=='overall':
        data=data[data.Medal.isin(['Gold','Silver','Bronze'])]    
    return data.Sex.value_counts().reset_index()