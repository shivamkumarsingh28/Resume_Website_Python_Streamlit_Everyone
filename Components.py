import streamlit as st
from streamlit_option_menu import option_menu

def top_menu():
    top_menu_select = option_menu(
        menu_title = None,
        options = ["Python", "Java", "Php", "JavaScript"],
        icons = ['house'],
        orientation= "horizontal"
    )
    return top_menu_select