import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page



current_page = st.sidebar.selectbox("Explore Or Predict", ("Explore", "Predict"))

if current_page == "Predict":
    show_predict_page()
else:
    show_explore_page()