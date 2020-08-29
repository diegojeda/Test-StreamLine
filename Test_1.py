
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pydeck as pdk

DATE_TIME = "date/time"
DATA_URL = (
    "http://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz"
)

st.title("Uber Pickups in New York Cityyyyyy")
st.markdown(
"""
This is a demo of a Streamlit app that shows the Uber pickups
geographical distribution in New York City. Use the slider
to pick a specific hour and look at how the charts change.
[See source code](https://github.com/streamlit/demo-uber-nyc-pickups/blob/master/app.py)
""")

@st.cache(persist=False)
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis="columns", inplace=True)
    data[DATE_TIME] = pd.to_datetime(data[DATE_TIME])
    return data


data = load_data(100000)

hour = st.sidebar.slider('hour', 0,23)

data=data[data[DATE_TIME].dt.hour==hour]

st.map(data)
'''
midpoint = (np.average(data["lat"]), np.average(data["lon"]))

st.write(pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    initial_view_state={
        "latitude": midpoint[0],
        "longitude": midpoint[1],
        "zoom": 11,
        "pitch": 50,
    },
    layers=[
        pdk.Layer(
            "HexagonLayer",
            data=data,
            get_position=["lon", "lat"],
            radius=100,
            elevation_scale=4,
            elevation_range=[0, 1000],
            pickable=True,
            extruded=True,
        ),
    ],
))
'''
'data',data

if (SB_Size=='All')&(SB_Type=='All')&(SB_Structure=='All')&(SB_Formation=='All'):
    # No filtros
    data=data
else:
    if(SB_Size=='All')&(SB_Type=='All')&(SB_Structure=='All'):# Filtramos Formacion
        data=data.loc[(data.Formation==SB_Formation)]
    if (SB_Size=='All')&(SB_Type=='All')&(SB_Formation=='All'):# Filtramos Estructura
        data=data.loc[(data.Structure==SB_Structure)]
    if (SB_Size=='All')&(SB_Structure=='All')&(SB_Formation=='All'):# Filtramos Tipo
        data=data.loc[(data.Type==SB_Type)]
    if (SB_Type=='All')&(SB_Structure=='All')&(SB_Formation=='All'):# Filtramos Tamaño
        SB_Size = float(SB_Size)
        data=data.loc[(data.Size==SB_Size)]
        st.write('Prueba de campo')
    
    if (SB_Size=='All')&(SB_Type=='All'):# Fitramos por formacion y por estructura
        data=data.loc[(data.Structure==SB_Structure)&(data.Formation==SB_Formation)]    
    if (SB_Size=='All')&(SB_Structure=='All'):# Filtramos por tipo y formacion
        data=data.loc[(data.Type==SB_Type)&(data.Formation==SB_Formation)]
    if (SB_Size=='All')&(SB_Formation=='All'):# Filtramos por tipo y por estructura
        data=data.loc[(data.Type==SB_Type)&(data.Structure==SB_Structure)]
    if (SB_Type=='All')&(SB_Structure=='All'):# Filtramos por tamaño y por formacion
        SB_Size = float(SB_Size)
        data=data.loc[(data.Size==SB_Size)&(data.Formation==SB_Formation)]
    if (SB_Type=='All')&(SB_Formation=='All'):# Filtramos por tamaño y estructura
        SB_Size = float(SB_Size)
        data=data.loc[(data.Size==SB_Size)&(data.Structure==SB_Structure)] 
    if (SB_Structure=='All')&(SB_Formation=='All'):# Filtramos tamaño y tipo
        SB_Size = float(SB_Size)
        data=data.loc[(data.Type==SB_Type)&(data.Size==SB_Size)]

    if (SB_Size=='All'): #Filtramos por tipo, estructura y formacion
        data=data.loc[(data.Type==SB_Type)&(data.Structure==SB_Structure)&(data.Formation==SB_Formation)]
    if (SB_Type=='All'): #Filtramos por tamaño, estructura y formacion
        SB_Size = float(SB_Size)
        data=data.loc[(data.Size==SB_Size)&(data.Structure==SB_Structure)&(data.Formation==SB_Formation)]
    if (SB_Structure=='All'):# Filtramos por tipo, tamaño y formacion
        SB_Size = float(SB_Size)
        data=data.loc[(data.Type==SB_Type)&(data.Size==SB_Size)&(data.Formation==SB_Formation)]
    if (SB_Formation=='All'): #Filtramos por tamaño, tipo y estructura
        SB_Size = float(SB_Size)
        data=data.loc[(data.Type==SB_Type)&(data.Size==SB_Size)&(data.Structure==SB_Structure)]




