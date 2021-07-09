import os
import app2
import streamlit as st
import pandas as pd
import pydeck as pdk
import numpy as np
from streamlit_folium import folium_static
import folium
import model
    

def app():

    st.title("Rapport des détéctions:")
    st.title("")
    df = pd.read_csv(model.files['data'])

    st.dataframe(df, width=1000, height=1000)    