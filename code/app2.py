import os
import streamlit as st
import pandas as pd
import pydeck as pdk
import numpy as np
from streamlit_folium import folium_static
import folium
import controller as ctrl
import model


def file_selector(folder_path='.'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Select a model version', filenames)
    return os.path.join(folder_path, selected_filename)


def app():

    st.title("Détection de déchets sur une image")
    img = st.file_uploader('Ajouter une image')
    
    user_input = st.text_input("Rentrer l'adresse où la photo à été prise :")
    
    if img != None:
        if st.button('Détecter les déchets'):
            imgs = []
            with st.spinner('Traitement en cours ...'):
                res_analysis = ctrl.analyze_image(img) 
                imgs.append(res_analysis['img'])
            
            st.success('Analyse terminé !')
            isDetected = False
            for elt in res_analysis['data'].values():
                if elt != 0:
                    isDetected = True

            if len(imgs) != 0 and isDetected == True:            
                info = ctrl.get_lat_long(user_input)

                st.header('Image avec toutes les détections :')
                st.image(imgs[0], use_column_width=True)
                st.header('Analyse :')
                st.text("Adresse : %s " % ','.join(info['full_address'].split(',')[:3]))
                st.text("Détails des détections sur l'image :")
                for key, val in res_analysis['data'].items():
                    if val != 0:    
                        st.text(f"{key} : {val}")

                
                df = ctrl.pd.read_csv(model.files['data'])
                for key, val in res_analysis['data'].items():
                    if val != 0:
                        rec = {'lat' : info['lat'], 'long' : info['long'], 'class' : key, 'qty' : val}

                        df = df.append(rec,ignore_index=True)
                df.to_csv(model.files['data'], index=False)
                st.success('Sauvegarde des données réussi')
     

            else:
                st.error("Notre modèle n'as rien détecté")