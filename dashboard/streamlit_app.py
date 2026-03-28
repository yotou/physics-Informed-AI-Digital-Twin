import streamlit as st
import requests

st.title("Digital Twin Monitoring")

temp = st.slider("Temperature",20,100,50)
vibration = st.slider("Vibration",0.0,1.0,0.3)

if st.button("Predict"):

    res = requests.post(
        "http://localhost:5000/predict",
        json={"temperature":temp,"vibration":vibration}
    )

    st.write(res.json())