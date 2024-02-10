#invoice Extarctor

from dotenv import load_dotenv

load_dotenv()  #load all the environemnt from .env

import streamlit as st
import os
from PIL import image
import google.generativeai as genai

#configure api key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

##function to load gemini pro visiion model

def get_gemini_response(input,image,prompt):  #this prompt we be my information i want to give
    #loading the gemini model
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input,image[0],prompt])
    return response.text