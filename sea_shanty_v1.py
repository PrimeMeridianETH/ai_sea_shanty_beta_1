# Install dependencies

# Import dependencies
import openai
import streamlit as st

# Set the OpenAI secret key
openai.api_key = st.secrets['pass']

st.header('Arrr-tificial Intelligence')
st.subheader('Present version be beta 0.1, ye scallywags!')

# Set the if, else loop including prompt
article_text = st.text_area('Avast, me hearty! Type in the words ye want to shanty!')
if len(article_text) > 5:
    temp = st.slider("Sea Shanty-ness", 0.2, 0.5, 0.8)
    if st.button ('Strike me a shanty, me hearties!'):
        response = openai.Completion.create(
            engine = "text-davinci-003",
            prompt = "You are an 'Arrr-tifcial Intelligence Model' that interprets text input and converts into a funny and relevant sea shanty. try to rhyme. Always use line breaks and proper prose. format is very important. Use only the text information located here: " + article_text,
            max_tokens = 3000,
            presence_penalty=0.8,
            frequency_penalty=0.6,
            temperature = temp
        )
        res = response["choices"][0]["text"]
        st.info(res)

        st.download_button("Download result", res)
else: st.warning("The provided details be not sizable enough, matey!")
