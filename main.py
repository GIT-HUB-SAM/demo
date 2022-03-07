import streamlit as st
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
from bokeh.plotting import figure

import pandas as pd
import numpy as np
import json

import base64
import time
import requests
from pprint import pprint

import panel as pn
pn.extension()

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
mapdata = pd.read_csv('map.csv')

with st.spinner('Loading the details...,'):
    time.sleep(1)


st.markdown("<h1 style='text-align: center;'>Demo App - Buysupply Interview</h1>", unsafe_allow_html=True)

st.markdown('<P style="text-align:justify;font-size:larger";><b>I built this application to demonstrate my skills in application developing. This application is built in Streamlit framework. '
            'Streamlit is an open-source app framework for Machine Learning and Data Science teams. It is pure Python framework, I have knowlege is other frameworks such as - '
            'Django and Flask. I have knowledge in handling API and Big Data, we can see the below application as example for such cases. Lets Go through one by one in Navigcation Menu...,'
            '</b></p>', unsafe_allow_html=True)

st.sidebar.title("Welcome to MyDashboard")
select = st.sidebar.selectbox("Navigation Menu", ("Resume", "Weather details","Data Table view", "Data Charts view","Demo Dashboard","Other Details"), key='1')

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

        #col1, col2, col3 = st.columns([3,3,3])
        #col1.metric("Weather in " + weather_data["name"] + " "+ systxt["country"],str(maintxt["temp"])+ " °C", 'today','off')
        # st.markdown("<h5>Today Weather in " + weather_data["name"] + " " + systxt["country"]  + '</h5><h1>' + str(maintxt["temp"]) + " °C</h1>", unsafe_allow_html=True)#col2.metric("Today Min", str(maintxt["temp_min"])+ " °C", "min temp")
        #st.markdown("<h5>Today Min  temp </h5><h1>" +  str(maintxt["temp_min"])+ " °C</h1>", unsafe_allow_html=True)
        #col3.metric("Today Max",str(maintxt["temp_max"])+ " °C" , "-max temp")
        #st.markdown("<h5>Today Max temp </h5><h1>" + str(maintxt["temp_max"])+ " °C</h1>", unsafe_allow_html=True)

        st.markdown('<!-- Latest compiled and minified CSS -->'
                '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">'
                '<!-- jQuery library -->'
                '<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>'
                '<!-- Latest compiled JavaScript -->'
                '<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>'
                '<table class="table table-bordered ">'
                '<thead>'
                '<tr>'
                '<th scope="col" class="col-md-2 info"><h4> Today Weather in '+ str(weather_data["name"])  + ' ' + systxt["country"] +'</h4></th>'
                '<th scope="col" class="col-md-2 success"><h4> Today Min temp </h4></th>'
                '<th scope="col" class="col-md-2 danger"><h4> Today Max temp </h4></th>'
                '</tr>'
                '</thead>'
                '<tbody>'
                '<tr>'
                '<th scope="row" class ="info"><h1>'+ str(maintxt["temp"]) +' °C<h1></th>'
                '<th scope="row" class ="success"><h1>'+ str(maintxt["temp_min"]) +' °C<h1></th>'
                '<th scope="row" class ="danger"><h1>'+ str(maintxt["temp_max"]) +' °C<h1></th>'                    
                '</tr>''</tbody>'
                '</table>',unsafe_allow_html=True)


        #col1, col2, col3, col4 = st.columns(4)
        #col1.metric("Weather Condition is ",weathertxt["main"], weathertxt["description"],'off')
        # col2.metric("visibility ", weather_data["visibility"])
        # col3.metric("Wind speed ", windtxt["speed"])
        #col4.metric("Humidity ", maintxt["humidity"])

        st.markdown('<!-- Latest compiled and minified CSS -->'
                    '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">'
                    '<!-- jQuery library -->'
                    '<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>'
                    '<!-- Latest compiled JavaScript -->'
                    '<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>'
                    '<table class="table table-bordered ">'
                    '<thead>'
                    '<tr>'
                    '<th scope="col" class="col-md-3"><h4> Weather Condition is '+ str(weathertxt["main"]) +'</h4></th>'
                    '<th scope="col" class="col-md-3 active"><h4> Visibility '+ str(weather_data["visibility"]) +'</h4></th>'
                    '<th scope="col" class="col-md-3"><h4> Wind speed  '+ str(windtxt["speed"]) +'</h4></th>'
                    '<th scope="col" class="col-md-3 warning"><h4> Humidity  '+ str(maintxt["humidity"]) +'</h4></th>'
                    '</tr>'
                    '</thead>'
                    '<tbody>'
                    '<tr>'
                    '<th scope="row"><h1>'+ str(weathertxt["description"]) +'<h1></th>'
                    '<th scope="row" class ="active"><h1>'+ str(weather_data["visibility"]) +'<h1></th>'
                    '<th scope="row"><h1>'+ str(windtxt["speed"]) +'<h1></th>'
                    '<th scope="row" class ="warning"><h1>'+ str(maintxt["humidity"]) +'<h1></th>'
                    '</tr>''</tbody>'
                    '</table>',unsafe_allow_html=True)

        st.title('Full JSON response')
        st.json(weather_data)


if select == 'Data Table view':
    st.title("Data Table view")
    st.error('Here we are going to view the demo data in Table format')

    df = pd.DataFrame(data)
    st.subheader("This is a table view")
    st.table(df.head(10))

    st.subheader("This is a dataframe view")
    st.dataframe(df.style.highlight_max(color='green', axis=0))
    st.caption("We have highlighted max value")

if select == 'Data Charts view':
    st.title("Data Charts view")
    st.warning('Here we have plotted some charts with demo data')

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
if select == 'Demo Dashboard':
    st.title("Demo Dashboard")
    st.info('Here we are seeing Dashboard with demo data')

    col1, col2 = st.columns([5,5])
    with col1:
        st.markdown("## **Item level analysis**")
        selectItem1 = st.selectbox('Select a Item', data['ItemType'], key= 1)
        selectItem2 = st.selectbox('Select a Item', data['ItemType'], key= 2)

        data_itemtype = data[data['ItemType'] == selectItem1]
        data_itemtype2 = data[data['ItemType'] == selectItem2]

        data_itemtype = data_itemtype.groupby('ItemType').mean()
        data_itemtype2 = data_itemtype2.groupby('ItemType').mean()

        data_itemtype = data_itemtype[["UnitCost", "TotalCost", "TotalRevenue", "TotalProfit"]]
        data_itemtype2 = data_itemtype2[["UnitCost", "TotalCost", "TotalRevenue", "TotalProfit"]]

        df = pd.concat([data_itemtype,data_itemtype2])
        st.write(df)
        st.area_chart(df)

    with col2:
        st.markdown("## **Country level analysis**")
        select = st.selectbox('Select a Country', data['Country'])

        select_data = data[data['Country'] == select]
        select_data = select_data.groupby('Country').mean()

        def get_total_dataframe(dataset):
            total_dataframe = pd.DataFrame({
                'Status': ['TotalProfit', 'TotalRevenue'],
                'Number of sales': (dataset.iloc[0]['TotalProfit'],
                                    dataset.iloc[0]['TotalRevenue'])})
            return total_dataframe


        select_total = get_total_dataframe(select_data)

        st.markdown("### Total Sales in the %s is" % (select))
        if not st.checkbox('Hide Graph', False, key=1):
            state_total_graph = px.bar(
                select_total,
                x='Status',
                y='Number of sales',
                labels={'Number of sales': 'total sales in %s' % (select)  },
                color='Status')
            st.plotly_chart(state_total_graph)

    st.subheader("Interactive Data with filter condition")

    num = st.number_input('Order and Shipping date filter', step=1)
    data['datadiff'] = (pd.to_datetime(data['ShipDate'], format='%m/%d/%Y') - pd.to_datetime(data['OrderDate'], format='%m/%d/%Y')).dt.days

    data_order = data[data['datadiff'] <= num]
    data_order = pd.DataFrame(data_order, columns=["ItemType","OrderID","OrderDate","ShipDate","datadiff"])
    hist_data = data_order.groupby(["ItemType"]).size().reset_index(name='count')

    if st.checkbox('Show Full Data', False, key=2):
        st.write(data)

    col1, col2 = st.columns([5, 5])
    with col1:
        st.caption("The below data is filtered by above condition")
        st.write(data_order.sort_values(by='datadiff', ascending=False))

    with col2:
        #fig, ax = plt.subplots()
        #ax.hist(data_order['datadiff'])
        #st.pyplot(fig)

        fig = px.line(
            df,  # Data Frame
            x=hist_data['ItemType'].values,  # Columns from the data frame
            y=hist_data['count'].values,
            title="Sales graph"
        )
        fig.update_traces(line_color="maroon")
        st.plotly_chart(fig)

    col1, col2 = st.columns([5,5])
    with col1:

        fig = go.Figure(
            go.Pie(
                labels=hist_data['ItemType'].values,
                values=hist_data['count'].values,
                hoverinfo="label+percent",
                textinfo="value",
                title="products sold"
            ))

        st.plotly_chart(fig)

    with col2:
        fig = px.pie(
            hole=0.7,
            names=hist_data['ItemType'].values,
            labels=hist_data['count'].values,
        )

        st.plotly_chart(fig)

    st.subheader("Map view")
    st.caption("This is demo data that shows in map view")
    chartmap = mapdata[["lat", "lon"]]
    #st.write(chartmap)
    st.map(chartmap)

if select == 'Other Details':
    st.title("Other Details for Interview Process")
    st.info('I have included this part for Interview Process')

    st.caption('Pleas find my answers below: ')


    st.markdown("<h3>Q: The job is contract & 100% Remote, Are you ok with that? </br> A: Yes, I am ok with the Remote Job.</h3>"
                "<h3>Q: What is your salary expectation?</br>"
                "A: I am getting $1000 Monthly in my previous job, I am expecting 30% hike from my previous Salary,</br>"
                "So I am expecting $1300 Monthly. Frequency can be Weekly, Bi Weekly or Monthly.</h3>"
                "<h3>Q: How many hours per week can you allocate? (Min & Max)</br>"
                "A: 30 - 60 Hours Weekly.</h3>"
                "<h3>Q: List out your PC/Laptop configuration & internet connection details </br>"
                "A: Processor : i5 10th gen</br>"
                "&nbsp; &nbsp; &nbsp;Memory : 32GB RAM / 500GB SSD</br>"
                "&nbsp; &nbsp; &nbsp;OS : Windows 10 64 bit</br>"
                "&nbsp; &nbsp; &nbsp;Internet Speed : 50 Mbps Upload and Download</h3>",unsafe_allow_html=True)


