import streamlit as st
import openai

openai.api_key = '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'

def get_joke(prompt):
    try:
        response = openai.chat.completions.create(
            model = "gpt-3.5-turbo",
            prompt = prompt,
            temperture = 0.5,
            max_tokens = 60,
            n = 1,
            stop = None,
            echo = False
        )
        joke = response.choices[0].text.strip()
        return joke 
    except Exception as e:
        return f"an error occured: {str(e)}"
    
st.title('Joke Suggestor with Chat GPT-3.5 Turbo')

user_prompt = st.text_input('Enter A Topic To Get A Joke About:' '')

if user_prompt: 
    joke = get_joke(user_prompt)
    st.markdown(f"**Joke:** {joke}")
else:
    st.write("Enter A Topic Above To Get A Joke")


        