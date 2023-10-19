import streamlit as st
import base64

#****************************background image##################
@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    print("hello")
    img = get_img_as_base64(png_file)
    page_bg_img = f'''
    <style>
        [data-testid="stAppViewContainer"] > .main {{
        background-image: url("data:image/png;base64,{img}");
        background-size: cover;
        background-position: top left;
        background-repeat: no-repeat;
        background-attachment: fixed;
        }}
    </style>
    '''
    
    st.markdown(page_bg_img,unsafe_allow_html=True)

set_png_as_page_bg("cato1234.jpeg")
#********************************************************************

colmn1 , colmn2 , colmn3 = st.columns(3)


username = colmn1.text_input("username",label_visibility="hidden",placeholder="Username")
# st.write(username)
password = colmn2.text_input ("password",label_visibility="hidden",placeholder="Password")
sidebar = st.sidebar
button = colmn1.button ("login")
