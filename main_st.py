import streamlit as st
import pandas as pd
import numpy as np
import requests

def api_call(user_data: dict, url:str = 'http://fastapi-app:8000/greet_user'):
    try:
        soltn = requests.post(url=url, json=user_data)
        soltn.raise_for_status()
        return soltn.json() 
    except requests.RequestException as e:
        print(f'Error connecting to greeting \n {e}')
        return None 




st.title("The Simplest Docker compose template for your apis")
st.write("Welcome to the test")


with st.sidebar:
    st.image("https://thumbnails.production.thenounproject.com/s3bI5zmkHfiQYrI53tM0VGCf8Os=/fit-in/1000x1000/photos.production.thenounproject.com/photos/4DAC2DA1-1A30-4D6F-92A7-C302AA5CD4CC.jpg")
    st.markdown("""
    ### Whale Hello There...
    """)

with st.form("Options"):
    st.write("Please enter your personal details below")
    age = st.slider("How old are you")
    first_name = st.text_input('What is your first name')
    submitted = st.form_submit_button("Submit")

if submitted:
    payload = {'first': first_name, 'age': age}

    greeting = api_call(payload)
    st.write(greeting)


    



