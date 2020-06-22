# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np 
import pickle 
import pandas as pd 
import streamlit as st 
from PIL import Image 


pickle_in = open("classifier.pkl","rb")
classifier = pickle.load(pickle_in)

def welcome():
    return "Welcome All"
def predict_note_authentication(variance,skewness,curtosis,entropy):
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return prediction


def main():
    st.title("Bank App Authenticator")
    html_temp ="""
     <div style="background-color:yellow;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    variance = st.text_input("Variance","Type Here")
    skewness = st.text_input("skewness","Type here")
    curtosis = st.text_input("curtosis","Type here")
    entropy = st.text_input("entropy","Type Here")
    result= ""
    if st.button("Predict"):
        result=predict_note_authentication(variance,skewness,curtosis,entropy)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    

