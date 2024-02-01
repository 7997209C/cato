
import base64
import streamlit as st

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

def hide_sidebar():
    st.markdown(
        """
    <style>
        [data-testid="collapsedControl"] {
            display: none
        }
    </style>
    """,
        unsafe_allow_html=True,
    )

def show_sidebar():
    st.markdown(
        """
    <style>
        [data-testid="collapsedControl"] {
            display: inline-block
        }
    </style>
    """,
        unsafe_allow_html=True,
    )