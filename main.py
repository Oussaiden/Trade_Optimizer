import streamlit as st
import sqlite3
st.set_page_config(
    page_title              ="Trade Optimizer",
    layout                  ="wide",  # Options: "centered" ou "wide"
    initial_sidebar_state   ="expanded",  # Options: "auto", "expanded", "collapsed"
)

from parametres.list import *


#Titre
st.markdown(
    """
    <h2 style="text-align: center;">Trade Optimizer</h2>
    """,
    unsafe_allow_html=True
)

with st.sidebar.expander("Indices"):
    # Sélection indice
    indice = list(indices.keys())
    affiche_indice = st.multiselect("",options=indice, key=None)