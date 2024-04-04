import streamlit as st
from openai import OpenAI


client = OpenAI(api_key='')

def get_joke(prompt):
    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "you are a drunk pirate"},
                {"role": "user", "content": prompt}
            ]
        )

        return completion.choices[0].message.content
    
    except Exception as e:
        return f"an error occured: {str(e)}"
    
st.title('Joke Suggestor with Chat GPT-3.5 Turbo')

user_prompt = st.text_input('Enter A Topic To Get A Joke About:' '')

if user_prompt: 
    joke = get_joke(user_prompt)
    st.markdown(f"**Joke:** {joke}")
else:
    st.write("Enter A Topic Above To Get A Joke")


        