import streamlit as st
from streamlit_extras.buy_me_a_coffee import button
from auth import auth_data
from helpers.utils import set_png_as_page_bg , hide_sidebar,show_sidebar
st.set_page_config(initial_sidebar_state="collapsed")
#****************************background image###################
set_png_as_page_bg("img/latestbg.jpeg")
#********************************************************************
#login form

#sidebar app
# with st.sidebar:
#     button(username='catocarling',floating=False)


def main():

    authenticator = auth_data()

    # login button
    name, authentication_status, username = authenticator.login('Login', 'main')

    if authentication_status:
        # button logout
        authenticator.logout('Logout', 'main')
        st.title('Welcome')
        show_sidebar()

    elif authentication_status == False:
        st.error('GET OUT OF MY WEBSITE YOU FILTHY ANIMAL')


    elif authentication_status == None:
        st.success('Welcome enter your username/password')

if __name__ == "__main__":
    hide_sidebar()
    st.image("img/logo.png")
    main()
  