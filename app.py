import streamlit as st
colmn1 , colmn2 , colmn3 = st.columns(3)


username = colmn1.text_input("username")
# st.write(username)
password = colmn2.text_input ("password")
sidebar = st.sidebar
button = colmn1.button ("login")