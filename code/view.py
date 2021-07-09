# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 15:28:28 2021

@author: vwork
"""

import streamlit as st
import pandas as pd
import pydeck as pdk
import app, app2, app3, app4
from model import PAGES

st.set_page_config(
        page_title = "Databage",
        page_icon= "/Users/rayane/Desktop/logo_databage/ico.ico",
        layout = "centered",
        initial_sidebar_state = "expanded",
    )


def DatabageView():
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio("Aller à", list(PAGES.keys()))
    page = PAGES[selection]
    page.app()
            
            


        