import streamlit as st
import pandas as pd
import joblib
import numpy as np
import os

# 1. Page Configuration
st.set_page_config(page_title="Employee Performance Predictor", layout="centered")

# 2. Header Section
st.title("📊 Employee Performance Predictor")
st.write("This dashboard predicts employee performance categories using a trained Random Forest model.")

# 3. Load the Trained Model
model_path = 'models/perf_model.pkl'

if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    st.error("Error: Trained model not found. Please run main.py first to generate the model file.")
    st.stop()

# 4. Sidebar for User Input
st.sidebar.header("Input Employee Metrics")

def user_input_features():
    years_exp = st.sidebar.slider("Years of Experience", 1, 15, 5)
    projects = st.sidebar.slider("Projects Handled", 1, 10, 3)
    attendance = st.sidebar.slider("Attendance Rate (%)", 60, 100, 85)
    training_score = st.sidebar.slider("Training Score", 40, 100, 75)
    
    data = {
        'years_exp': years_exp,
        'projects': projects,
        'attendance': attendance,
        'training_score': training_score
    }
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

# 5. Display Input Summary
st.subheader("Input Summary")
st.write(input_df)

# 6. Prediction Logic
if st.button("Run Prediction"):
    prediction = model.predict(input_df)
    
    # Mapping results: 0 -> Low, 1 -> Medium, 2 -> High
    performance_map = {0: "Low Performer", 1: "Medium Performer", 2: "High Performer"}
    result = performance_map[prediction[0]]
    
    # Display Result with styling
    st.subheader("Prediction Result:")
    if prediction[0] == 2:
        st.success(f"Result: {result} 🚀")
    elif prediction[0] == 1:
        st.info(f"Result: {result} 📈")
    else:
        st.warning(f"Result: {result} ⚠️")

# 7. Dataset Preview
if st.checkbox("Show Training Data Sample"):
    if os.path.exists('data/employee_data.csv'):
        df_sample = pd.read_csv('data/employee_data.csv')
        st.write(df_sample.head())
    else:
        st.write("Dataset file not found.")