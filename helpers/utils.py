
import base64
import streamlit as st

@st.cache_data
def get_base64_of_bin_file(bin_file):
    with open(bin_file,   'rb') as f:
        data =f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = f'''
    <style>
    body{{
    background-image: url("data:image/png;base64,{bin_str}");
    background-size: cover;
    }}
    </style>
    '''
    st.markdown(page_bg_img,unsafe_allow_html=True)