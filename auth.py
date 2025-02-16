import streamlit as st
import streamlit_authenticator as au
import yaml
from yaml.loader import SafeLoader
# hashed_passwords = au.Hasher(['abc', 'def']).generate()
# st.write(hashed_passwords)

def auth_data():
    with open('config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)

    authenticator = au.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
    )

    return authenticator

def username_data():
    with open('config.yaml') as file:
        return yaml.load(file, Loader=SafeLoader)

    