# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 15:28:28 2021

@author: vwork
"""


import streamlit as st
import controller as ctrl


def DatabageView():
    st.title('Welcome to Databage')
    st.text('a ML garbage detection by Vaihau, Maxime, Hugo, Rayane, Ines and Ahmed')

    st.header("Détection de déchets sur une image")
    img = st.file_uploader('Ajouter une image')
    
    
    if img != None:
        st.image(img, use_column_width=True)
        
        btn_analysis = st.button('Détecter les déchets')
        if btn_analysis:
            imgs = []
            with st.spinner('Traitement en cours ...'):
                imgs.append(ctrl.analyze_image(img))

            st.success('Détection terminé !')

            if len(imgs) != 0:            
                st.header('Image avec toutes les détections :')
                st.image(imgs[0], use_column_width=True)
            else:
                st.error('Une erreur est survenu veuillez relancer la détection')


        