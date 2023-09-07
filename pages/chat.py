import streamlit as st

with st.sidebar:
    username = st.text_input("say your username")

message = st.chat_input("say somthing")
if message:
    st.write(f"{username} :  {message}")

   