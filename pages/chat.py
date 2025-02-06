import streamlit as st
import json
import os
from helpers.utils import hide_sidebar
import app 
# st.text_input ("input email or phone number")

# with st.sidebar:
#     username = st.text_input("say your username")
#     avatar = st.radio("choose your avatar",["🐨","🐬","🐲"],index=0,horizontal=True)

# message = st.chat_input("talk to someone")
# if message:
#     with st.chat_message("cato",avatar = avatar):
#         st.write(f"{username} :  {message}")

# st.button ("press to save")
##########################################chat###########################


# Function to load and save chat messages
def load_chat_messages(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    else:
        return []
def save_chat_message(filename, message_data):
    messages = load_chat_messages(filename)
    messages.append(message_data)
    with open(filename, "w") as file:
        json.dump(messages, file)

def main():
    hide_sidebar()
    st.title("Chat")

    # Input for username
    # username = st.text_input("Enter your username", "")
    # st.header("your name is", {app.username})
    # app.username
    st.title(f'Welcome {app.username}')
    # File to store chat messages
    filename = "chat_messages.json"

    # Display previous messages
    messages = load_chat_messages(filename)
    for message_data in messages:
        author = message_data["username"]
        message = message_data["message"]
        with st.chat_message(author):
            st.write(f"{author}: {message}")

    # Chat input for new message
    new_message = st.chat_input("Send a message")

    

    # Handle new message
    if new_message and username:
        save_chat_message(filename, {"username": username, "message": new_message})
        st.rerun()  # Rerun the app to refresh the messages

if __name__ == "__main__":
    main()
