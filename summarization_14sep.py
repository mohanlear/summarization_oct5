# Agenda: 
# How to use LLMs for summarization, sentiment, topic analysis for any news article/text content using streamlit.
# input: news article/ text content
# output: summarize in limited words , classify bad or good
# A summary of the input article, any sentiment on the article,
# Approach: 
# 1. fetch the text content -> [an interface, paste the content] - streamlit
# 2a. load from .env and test the llm
# 2b. create a customized prompt [system prompt + user text data [context] + output format]
# 3. customized prompt -> llm -> output -> show it to user
# code
# Streamlit -> 
# to run from terminal
# $ pip install streamlit
# $ pip install google-generativeai
# https://streamlit.io/ [for reference]
# to stop the server [ctr+c]


import streamlit as st
st.title("Summarization application")
## to provide a provision for user to enter the text content
user_text = st.text_area("Enter the text content to analyze sentiment:")
print("user provided content",user_text)
# is streamlit can be hosted only locally
# Is Streamlit open source - open source -> 
# Is it for just for demo purpose or can I develop enterprise level application?

# 
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("api_key")
# initialize an LLM
import google.generativeai as genai
# Configure
genai.configure(api_key=api_key)
# Pick Gemini model
model = genai.GenerativeModel("gemini-2.0-flash-lite") # responses are super fast, accuracy can be low

prompt = '''Your an an expert in Summarization. Summarize the text content below in a sentence:
Text: 
'''
# how do we get summarized content in 1-2 sentences?
# use a restrict parameter - prompt
# You can clearly mention the output format and length
# fine tune LLm parameters
# As a content expert can you summarize it in a crytal clear manner not more then 20-30 words . and use the content ""

final_prompt = prompt + user_text
## response
response = model.generate_content(
    final_prompt,     
generation_config={
        "temperature": 0.01,         # lower = more deterministic
        "max_output_tokens": 60    # restricts length
        #"top_p": 0.1,
    }
)
print("out", response.text)
st.write(response.text)


# text_need = st.text_input("enter a nlp task:")

# # how do we get summarized content in 1-2 sentences?
# # use a restrict parameter - prompt
# # You can clearly mention the output format and length
# # fine tune LLm parameters
# # As a content expert can you summarize it in a crytal clear manner not more then 20-30 words . and use the content ""

# ## response
# response = model.generate_content(
#     text_need,     
# generation_config={
#         "temperature": 2,         # lower = more deterministic
#         "max_output_tokens": 100    # restricts length
#         #"top_p": 0.1,
#     }
# )
# print("out", response.text)
# st.write(response.text)
