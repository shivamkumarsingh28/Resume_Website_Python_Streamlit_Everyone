import streamlit as st
import sidebar, Components

# sidebar menu 
Sidebar_Menu =sidebar.sidebar_menu()

if Sidebar_Menu == "Intro":
    st.title("Introduction page here")

if Sidebar_Menu == "Education":
    st.title(Sidebar_Menu)

if Sidebar_Menu == "Experience":
    st.title(Sidebar_Menu)

if Sidebar_Menu == "Achievement":
    st.title(Sidebar_Menu)

if Sidebar_Menu == "Other":
    st.title(Sidebar_Menu)



# Project page config here
if Sidebar_Menu == "Project":
    # top menu 
    Top_Menu = Components.top_menu()
    if Top_Menu == "Python":
        st.title(Top_Menu)

    if Top_Menu == "Php":
        st.title(Top_Menu)

    if Top_Menu == "Java":
        st.title(Top_Menu)

    if Top_Menu == "JavaScript":
        st.title(Top_Menu)
