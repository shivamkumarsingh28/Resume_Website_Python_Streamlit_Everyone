import streamlit as st
from streamlit_option_menu import option_menu

def sidebar_menu():
    with st.sidebar:
        sidebar_select = option_menu(
            menu_title = "Your name Here - resume", 
            options = ["Intro", "Project", "Education", "Experience", "Achievement", "Other"], #Menu here
            icons = ['house'] #icons here
        )
    return sidebar_select