import streamlit as st
import requests

st.title("AI Data Quality Copilot")

if st.button("Analyze Dataset"):

    response = requests.get("http://127.0.0.1:8000/analyze")

    data = response.json()

    st.subheader("Dataset Profile")
    st.write(data["profile"])

    st.subheader("Issues Detected")
    st.write(data["issues"])

    st.subheader("AI Explanation")
    st.write(data["ai_report"])