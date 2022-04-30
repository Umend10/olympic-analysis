import streamlit as st
import pandas as pd
import preprocess
import helper
import seaborn as sns
import matplotlib.pyplot as plt
event1=pd.read_csv("athlete_events.csv")
country=pd.read_csv("noc_regions.csv")

#title ob=f preject
st.sidebar.header("Olympic Analysis")

user_menue=st.sidebar.radio(
    "Select An Option",
    ('Medal Tally','Overall Analysis','Country wise Analysis','Athelete wise Analysis')
)

data=preprocess.transform(event1,country)

#st.dataframe(data)


if user_menue=='Medal Tally':
    st.sidebar.header("Medal Tally")
    year,country=helper.country_year_lsit(data)
    selected_year=st.sidebar.selectbox("select year",year)
    select_country=st.sidebar.selectbox("select country",country)
    medal_tally=helper.medal_tally(data,selected_year,select_country)
    if selected_year=='overall' and select_country=='overall':
        st.title("Overall")
    if selected_year!='overall' and select_country=='overall':
        st.title('Medal Tallly in '+ str(selected_year) + ' Olympic')
    if selected_year=='overall' and select_country!='overall':
        st.title(select_country +' overall performance')
    if selected_year!='overall' and select_country!='overall':
        st.title(select_country+'performance in '+str(selected_year)+' olympics')
    st.table(medal_tally)
if user_menue=='Overall Analysis':
    Edition=data.Year.unique().size-1
    Hosts=data.City.unique().size
    Sport=data.Sport.unique().size
    Event=data.Event.unique().size 
    Nation=data.region.unique().size
    Athelits=data.Name.unique().size
    st.title("Top Statistics")
    col1,col2,col3=st.columns(3)
    with col1:
        st.header("Edition")
        st.title(Edition)
    with col2:
        st.header("Hosts")
        st.title(Hosts)
    with col3:
        st.header("Sports")
        st.title(Sport)
    col1,col2,col3=st.columns(3)

    with col1:
        st.header("Events")
        st.title(Event)
    with col2:
        st.header("Nation")
        st.title(Nation)
    with col3:
        st.header("Athelits")
        st.title(Athelits)
    
    st.header("Participating nation over the year")
    particiapt_Country=helper.graph(data,'region')
    fig = plt.figure(figsize=(12,10))
    sns.lineplot(data=particiapt_Country,x='Year',y='region')
    st.pyplot(fig)

    st.header("Participating athelits over the year")
    particiapt_Country=helper.graph(data,'Name')
    fig = plt.figure(figsize=(12,10))
    sns.lineplot(data=particiapt_Country,x='Year',y='Name')
    st.pyplot(fig)

    st.header("Event over the year")
    particiapt_Country=helper.graph(data,'Event')
    fig = plt.figure(figsize=(12,10))
    sns.lineplot(data=particiapt_Country,x='Year',y='Event')
    st.pyplot(fig)

    st.header('Event Happen on Year')
    hit=helper.heatmap(data)
    fig=plt.figure(figsize=(20,20))
    sns.heatmap(hit,annot=True)
    st.pyplot(fig)

    st.header("Top 15 athletes")
    sport=helper.Sport_name(data)
    select=st.selectbox('Select Sport',sport)
    athelit=helper.athelit(data,select)
    st.table(athelit)

#Country wise medal tally

if user_menue=='Country wise Analysis':
    st.header("Country wise medal")
    year,country=helper.country_year_lsit(data)
    country=st.sidebar.selectbox('Select Country',country[1:])
    st.sidebar.header(country +" Medal Tally Over Year")
    country_wise=helper.country_name_analysis(data,country)
    fig=plt.figure(figsize=(12,8))
    sns.lineplot(data=country_wise,x="Year",y="Medal")
    st.pyplot(fig)
    #del country   
    
    #year,country_1=helper.country_year_lsit(data)
    #country=st.selectbox('Select Country',country_1)  
    st.header('Heatmap for '+country) 
    fig=plt.figure(figsize=(20,20))
    heatmap_data=helper.medal_analysis_county_wise_hitmap(data,country)
    sns.heatmap(heatmap_data,annot=True)
    st.pyplot(fig)



##top 15 athletes
    st.header("Top athletes those won medal for "+country)
    sport=helper.Sport_name(data)
    select=st.selectbox("Select Sport Name",sport)
    top_15=helper.athlete_by_country(data,country,select)
    st.table(top_15)

if user_menue=='Athelete wise Analysis':
    st.header("Age wise medal Analysis")
    medal_type=st.sidebar.selectbox("select medal type ",['Gold','Silver','Bronze','participate','overall'])
    st.sidebar.header(medal_type)
    medal_data=helper.medal_dist_on_age(data,medal_type)
    fig=plt.figure(figsize=(13,10))
    sns.distplot(medal_data)
    st.pyplot(fig)

    # weight wise medal analysis
    st.header('Weight wise medal analysis')
    medal_data=helper.medal_dist_on_weight(data,medal_type)
    fig=plt.figure(figsize=(13,10))
    sns.distplot(medal_data)
    st.pyplot(fig)

    #height wise medal analysis
    st.header('height wise medal analysis')
    medal_data=helper.medal_dist_on_height(data,medal_type)
    fig=plt.figure(figsize=(13,10))
    sns.distplot(medal_data)
    st.pyplot(fig)
    
    st.header('gender wise medal analysis')
    medal_data=helper.medal_dist_on_gender(data,medal_type)
    fig=plt.figure(figsize=(13,10))
    sns.barplot(x=medal_data.index,y=medal_data.Sex)
    fig1=plt.legend(["Male",'Female'])
    st.pyplot(fig,fig1)







    

    
    


    
