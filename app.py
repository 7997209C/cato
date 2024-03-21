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
        c1,c2,c3,= st.columns(3)
        with c2: 
            st.title(f'Welcome {username}')
            url = 'https://robohash.org/' + username
            st.image(url,use_column_width=True)
            # show_sidebar()
            st.divider()
            # url="http://ccmessage.streamlit.app/chat"
            #st.link_button("click me" , url="http://localhost:8501/chat" , use_container_width=True)
            st.page_link("pages/chat.py", label=" :red[Start Chatting ] ",icon="🗨️", use_container_width=True)
            authenticator.logout('Logout', 'main')
           
            
        # with st.form ("new chat form"):
        #     st.write ("what color is the sky?")
        #     x = st.checkbox("pink")
        #     y = st.checkbox("blue")
        #     clicked = st.form_submit_button ("New Chat")

        #     if clicked:
        #         if y:
        #             st.write ("you got it")
        #         else:
        #             st.write("loser")
        
        # st.checkbox("testing")
        

            
        # all_username = username_data()
        # search= st.selectbox("invite your friends into your chat here!",)


    elif authentication_status == False:
        st.error('GET OUT OF MY WEBSITE YOU FILTHY ANIMAL')


    elif authentication_status == None:
        st.success('Welcome enter your username/password')

if __name__ == "__main__":
    hide_sidebar()
    st.image("img/logo.png")
    main()