import streamlit as st

st.text_input ("input email or phone number")

with st.sidebar:
    username = st.text_input("say your username")
    avatar = st.radio("choose your avatar",["🐨","🐬","🐲"],index=0,horizontal=True)

message = st.chat_input("talk to someone")
if message:
    with st.chat_message("cato",avatar = avatar):
        st.write(f"{username} :  {message}")

st.button ("press to save")