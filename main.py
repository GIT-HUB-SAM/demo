import streamlit as st
import plotly.figure_factory as ff

import pandas as pd
import numpy as np
import json

import base64
import time
import requests
from pprint import pprint

st.set_page_config(
     page_title="My Demo App",
     page_icon="🧊",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://www.google.com',
         'Report a bug': "https://www.google.com",
         'About': "# This is a demo application made with streamlit. This is an *extremely* cool app!"
     }
 )

#st.balloons()

data = pd.read_csv('demodata.csv')

with st.spinner('Loading the details...,'):
    time.sleep(1)


st.markdown("<h1 style='text-align: center;'>Demo App - Buysupply Interview</h1>", unsafe_allow_html=True)
st.text('This is some text.')

st.sidebar.title("Welcome to MyDashboard")
select = st.sidebar.selectbox("Navigation Menu", ("Resume", "Weather details","Data Table view", "Data Charts view"), key='1')

if select == 'Resume':
    st.title("My Resume")
    st.success('Here we have rendered the PDF file')
    # Opening file from file path
    with open('Sudalai Resume.pdf', "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    pdf_display = F'<p align="justify"><iframe src="data:application/pdf;base64,{base64_pdf}" width="1100" height="1100" type="application/pdf"></iframe></p>'

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)

if select == 'Weather details':
    st.title("Weather details")
    st.subheader('Here we use openweathermap API to get the weather details')
    form = st.form(key='my_form')
    location = form.text_input(label='Enter Location',value='Chennai')
    submit_button = form.form_submit_button(label='Submit')

    if submit_button:
        st.subheader(f'Entered location:  {location}')
        weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid=3d8bfcb5ec27e4270d2c8d57443aa62d&units=metric"
        weather_data = requests.get(weather_url).json()

        #for keys,values in weather_data.items():
            #txt = st.write('{} : {}'.format(keys, values))
            #st.write("Weather data",txt)

        maintxt = {}
        maintxt  = weather_data["main"]
        systxt = weather_data["sys"]
        weathertxt = weather_data["weather"][0]
        windtxt = weather_data["wind"]


        col1, col2, col3 = st.columns(3)
        col1.metric("Weather in " + weather_data["name"] + " "+ systxt["country"],str(maintxt["temp"])+ " °C", 'today','off')
        col2.metric("Today Min", str(maintxt["temp_min"])+ " °C", "min temp")
        col3.metric("Today Max",str(maintxt["temp_max"])+ " °C" , "-max temp")

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Weather Condition is ",weathertxt["main"], weathertxt["description"],'off')
        col2.metric("visibility ", weather_data["visibility"])
        col3.metric("Wind speed ", windtxt["speed"])
        col4.metric("Humidity ", maintxt["humidity"])


        st.title('Full JSON response')
        st.json(weather_data)


if select == 'Data Table view':
    st.title("Data Table view")
    st.info('Here we are going to view the demo data in Table format')

    df = pd.DataFrame(data)
    st.subheader("This is a table view")
    st.table(df.head(10))

    st.subheader("This is a dataframe view")
    st.dataframe(df.style.highlight_max(color='green', axis=0))
    st.caption("We have highlighted max value")

if select == 'Data Charts view':
    st.title("Data Charts view")
    st.info('Here we have plotted some charts with demo data')

    chart_data1 = pd.DataFrame(data, columns=["Region", "UnitsSold"])
    chart_data1 = chart_data1.groupby('Region')[['UnitsSold']].sum()

    chart_data2 = pd.DataFrame(data, columns=["Country", "UnitsSold"])
    chart_data2 = chart_data2.head(50)
    chart_data2 = chart_data2.groupby('Country')[['UnitsSold']].sum()

    chart_data3 = pd.DataFrame(data, columns=["ItemType", "TotalRevenue","TotalCost","TotalProfit"])
    chart_data3 = chart_data3.groupby('ItemType')[["TotalRevenue","TotalCost","TotalProfit"]].sum()

    st.bar_chart(chart_data1,use_container_width = True)
    st.bar_chart(chart_data2,use_container_width = True)
    st.bar_chart(chart_data3,use_container_width = True)

    chart_data4 = pd.DataFrame(data, columns=["ItemType", "TotalProfit"])
    chart_data4 = chart_data4.groupby('ItemType')[["TotalProfit"]].sum()

    st.line_chart(chart_data4,use_container_width = True)

