import os
import streamlit as st
import pandas as pd
import pydeck as pdk
import numpy as np
from streamlit_folium import folium_static
import folium
import app2
import model


def app():
    st.title("Carte des déchets détectés:")
    st.title("")
    df = pd.read_csv(model.files['data'])
    dfmap = df[['lat', 'long']].rename(columns={"long" : "lon"})
    

    INITIAL_VIEW_STATE = pdk.ViewState(
        latitude=df.tail(1).iloc[0]['lat'],
        longitude=df.tail(1).iloc[0]['long'],
        zoom=10)               

    trash_layer = pdk.Layer("HeatmapLayer",data= df ,opacity=0.9,get_position=["long", "lat"],
        threshold=0.03,get_weight="qty",pickable=True)
    
    trash_deck = pdk.Deck(layers= [trash_layer], 
        initial_view_state= INITIAL_VIEW_STATE,
        map_provider="mapbox", map_style=pdk.map_styles.SATELLITE,
        tooltip={"text":"Concentration de déchets"})
    
    placeholder = st.empty()
    placeholder2 = st.empty()
    m2 = st.checkbox("Show heatmap")

    if m2:
        st.pydeck_chart(trash_deck)
    else:
        st.map(dfmap)
        