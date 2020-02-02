"""this file imports data of the X-Box game Fifa, in which the players are ranked according to their various playing skills such as shooting, passing, speed etc,
and also given a generic overall ranking. I have taken and plot some of the statistics of the players in a rolling-board fashion, taking 20 players at a time, out of total 1500 players"""


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time
import re
from PIL import Image


st.markdown("<h3></h3>",unsafe_allow_html=True)
st.markdown("<h3></h3>",unsafe_allow_html=True)
st.markdown("<h3></h3>",unsafe_allow_html=True)

st.title("The GAME is ON!")
st.markdown("<h3></h3>",unsafe_allow_html=True)

image = Image.open("img13.jpg")
st.image(image ,width = 900, format="JPEG")#,caption="The GAME is ON!")

st.markdown("<h3></h3>",unsafe_allow_html=True)
st.markdown("<h3></h3>",unsafe_allow_html=True)
st.markdown("<h3></h3>",unsafe_allow_html=True)


st.header("Data~")
st.markdown("<h3></h3>",unsafe_allow_html=True)
#function to fetch data from the csv file
@st.cache()
def fetch_data(file_location,rows):
    df = pd.read_csv(file_location,nrows=rows)
    df = df[['Name', "Nationality","Club", 'Overall', 'Value', 'Crossing', 'Finishing', 'Dribbling', 'BallControl', 'Acceleration', 'SprintSpeed', 'Penalties', 'GKHandling']]
    df.set_index("Name")
    return df

#fifa = 'C:/Users/rujua1/Desktop/Coding/Streamlit/'
rows=600
df1 = fetch_data('data.csv',rows)
table1 = st.write(df1)

st.markdown("<h3></h3>",unsafe_allow_html=True)
st.markdown("<h3></h3>",unsafe_allow_html=True)

image = Image.open("img3.jpg")
st.image(image ,width = 600, format="JPEG")#,caption="The GAME is ON!")
#st.write(df1.describe())

st.markdown("<h3></h3>",unsafe_allow_html=True)
st.markdown("<h3></h3>",unsafe_allow_html=True)
st.markdown("<h3></h3>",unsafe_allow_html=True)


st.header("Parameters~")
st.markdown("<h3></h3>",unsafe_allow_html=True)

df_list = st.multiselect("Select parameters that you want to compare",
                         ['Overall', 'Value', 'Crossing', 'Finishing', 'Dribbling', 'BallControl', 'Acceleration', 'SprintSpeed', 'Penalties', 'GKHandling']
                         )
#df_list = [str(x) for x in df_list]
df_list.append("Name")
df2 = (df1[df_list])
df2.set_index("Name")
df_temp = df2.iloc[0:20]
#st.write(df_list,type(df_list))
#display only selected statostic

#plot1 = plt.bar(data=df1, x='Name',height =10, stacked='True')
#plot1 = sns.barplot(data=df_temp,stacked=True)
if(st.button("Simulate")):
    st.header("Point Chart")
    plot1 = df_temp.plot(kind='bar', x='Name', stacked='True')
    fig = plt.gcf()
    fig.set_size_inches(10, 8)

    #plot1.figure()
    axes = plt.gca()
    #axes.set_ylim([0,800])

    plot21 = st.pyplot()
    progress_bar = st.progress(0)

    for i in range(0,len(df2.index),20):
        # Update progress bar.
        #status_text.text('Progress: ', i/1500*100)

        st.spinner(text="Ongoing")
        df_temp = df2.iloc[i:i+20]

        #plot1 = sns.barplot(data=df_temp,stacked=True)

        plot1 = df_temp.plot(kind='bar', x='Name', stacked='True')
        fig = plt.gcf()
        fig.set_size_inches(10, 8)

        #plot1.figure()
        axes = plt.gca()
        #axes.set_ylim([0, 800])

        plot21.pyplot()
        progress_bar.progress(i/rows)

    progress_bar.progress(100)
    with st.spinner('Wait for it...'):
        time.sleep(2)
    st.success('Done!')
    st.balloons()



tab1 = df1
st.sidebar.header("Search")
str_search = st.sidebar.text_input("Enter Player Name:")

#return df1[str_ser.upper() in df1["Name"].upper()]

def name_search(str_ser):
    for i in range(len(df1.index)):
        if(str(str_ser.upper()) in str((df1.iloc[i]["Name"]).upper())):
            return i
    return None
    #for x in df1['Name']:
     #   if str_ser.upper() in str(x).upper():
      #      return
if(st.sidebar.button('GO')):
    ind = name_search(str_search)
    #result=st.empty()
    #st.write(type(ind))

    st.sidebar.header("Player Search~")
    try:
        st.sidebar.table(tab1.iloc[ind])
    except TypeError:
        st.sidebar.error("Player not found")

#Filters
st.markdown("<h3></h3>",unsafe_allow_html=True)
st.markdown("<h3></h3>",unsafe_allow_html=True)
st.markdown("<h3></h3>",unsafe_allow_html=True)

st.sidebar.header("Filter")
st.markdown("<h3></h3>",unsafe_allow_html=True)

grp = st.sidebar.multiselect("Select parameter to Filter:",['Nationality','Club','Overall'])
nations_list = df1["Nationality"].unique()
clubs_list = df1["Club"].unique()


tab1=df1

#filter by Nationality
if("Nationality" in grp):
    st.sidebar.subheader("Country")
    choice = st.sidebar.selectbox("",nations_list)
    tab1 = tab1[tab1["Nationality"]==choice]

#filter by Club
if("Club" in grp):
    st.sidebar.subheader("Club")
    choice = st.sidebar.selectbox("",clubs_list)
    tab1 = tab1[tab1["Club"]==choice]

#to filter by range of Overall Rating
df1["Overall"]=df1["Overall"].astype('int')
if('Overall' in grp):
    st.sidebar.subheader("Overall Rating")
    (lb,ub) = st.sidebar.slider("Minimum Overall rating:",int(tab1["Overall"].unique().min()),int(tab1["Overall"].unique().max()),
                                                                                                  (int(tab1["Overall"].unique().min()),int(tab1["Overall"].unique().max())))

  #  ub = st.sidebar.slider("Maximum Overall rating:",int(tab1["Overall"].unique().min()),int(tab1["Overall"].unique().max()))
    df_lower = tab1[lb<=tab1["Overall"]]
    tab1 = df_lower[df_lower["Overall"]<=ub]


image = Image.open("img2.jpg")
st.image(image ,width = 600, format="JPEG")#,caption="The GAME is ON!")

st.markdown("<h3></h3>",unsafe_allow_html=True)
st.markdown("<h3></h3>",unsafe_allow_html=True)
st.markdown("<h3></h3>",unsafe_allow_html=True)


st.header("Filtered Table~")
st.markdown("<h3></h3>",unsafe_allow_html=True)
st.write(tab1)

st.markdown("<h3></h3>",unsafe_allow_html=True)
st.markdown("<h3></h3>",unsafe_allow_html=True)
st.markdown("<h3></h3>",unsafe_allow_html=True)

image = Image.open("img4.jpg")
st.image(image ,width = 600, format="JPEG")



#st.time_input('Date:')
#st.sidebar.header("Filter in Range:")
#grp1 = st.sidebar.radio('Select parameter to filter by:',['Value','Overall'])
