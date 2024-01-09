import streamlit as st
import base64
from streamlit_extras.buy_me_a_coffee import button
#****************************background image###################
@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    img = get_img_as_base64(png_file)
    page_bg_img = f'''
    <style>
        [data-testid="stAppViewContainer"] > .main {{
        background-image: url("data:image/png;base64,{img}");
        background-size: cover;
        background-position: top center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        }}
    </style>
    '''
    
    st.markdown(page_bg_img,unsafe_allow_html=True)

<<<<<<< HEAD
set_png_as_page_bg("img/bg.png")
=======
set_png_as_page_bg("img/christmas_background.jpg")
>>>>>>> 78b69e9b02c088daa2c92642738c67e59826a0f4
#********************************************************************
#login form

username = st.text_input("username",label_visibility="hidden",placeholder="Username")
# st.write(username)
<<<<<<< HEAD
password = st.text_input ("password",label_visibility="hidden",placeholder="Password")
=======
password = colmn2.text_input ("password",label_visibility="hidden",placeholder="Password")
# st.write(password)
>>>>>>> 78b69e9b02c088daa2c92642738c67e59826a0f4
button_loging = st.button ("login")

#sidebar app
with st.sidebar:
    button(username='catocarling',floating=False)

helo = st.text_input ("enter an number") 
mom = st.text_input ("enter a second number")

st.title(helo)
st.title(mom)

def hi (n,m):
    st.title(n+m)
    
hi (helo,mom)
