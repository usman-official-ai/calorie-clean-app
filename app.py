import streamlit as st
import pandas as pd
import pickle
import google.generativeai as genai

st.set_page_config(page_title="Calorie Predictor")
st.title("AI-Powered Calorie Burn Predictor")

@st.cache_resource
def load_models():
    model = pickle.load(open("calorie_model.pkl", "rb"))
    scaler = pickle.load(open("scaler.pkl", "rb"))
    return model, scaler

@st.cache_resource
def load_gemini():
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            return genai.GenerativeModel(m.name)
    return None

model, scaler = load_models()
gemini_model = load_gemini()

def predict(text):
    prompt = f"Extract Age, Gender(Male/Female), Height(cm), Weight(kg), Duration(min), Heart Rate(bpm) from: '{text}'. Return: Age Gender Height Weight Duration Heart Rate"
    response = gemini_model.generate_content(prompt)
    vals = response.text.strip().split()
    try:
        age = float(vals[0])
        gender = 1 if vals[1].lower() == 'male' else 0
        height = float(vals[2])
        weight = float(vals[3])
        duration = float(vals[4])
        heart = float(vals[5])
        bmi = weight / ((height/100)**2)
        df_input = pd.DataFrame([[age, gender, height, weight, duration, heart, bmi]],
                                columns=['Age','Gender','Height','Weight','Duration','Heart_Rate','BMI'])
        scaled = scaler.transform(df_input)
        cal = model.predict(scaled)[0]
        return cal, {'Age':age,'Gender':vals[1],'Height':height,'Weight':weight,'Duration':duration,'Heart_Rate':heart}
    except:
        return None, None

user_text = st.text_area("Describe your workout", height=100)

if st.button("Predict Calories"):
    if user_text:
        cal, feat = predict(user_text)
        if cal:
            st.success(f"Predicted Calories: {cal:.1f} kcal")
            with st.expander("Details"):
                st.json(feat)
        else:
            st.error("Try: 22 male 175cm 68kg cycled 35min heart rate 145")
    else:
        st.warning("Please describe your workout.")