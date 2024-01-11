import streamlit as st
import streamlit_authenticator as au
import yaml
from yaml.loader import SafeLoader

# hashed_passwords = au.Hasher(['abc', 'def']).generate()
# st.write(hashed_passwords)


with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = au.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)
name, authentication_status, username = authenticator.login('Login', 'main')
if authentication_status:
    authenticator.logout('Logout', 'main')
    st.write(f'Welcome *{name}*')
    st.title('Some content')
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')

    