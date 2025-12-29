import streamlit as st
import numpy as np
import sys
import os

# 🔥 FIX: add src folder to Python path
sys.path.append(os.path.abspath("src"))

from data_loader import load_data, split_data
from model import train_model
from evaluate import evaluate_model

# -----------------------------
# UI
# -----------------------------
st.set_page_config(page_title="Iris Flower Classification", page_icon="🌸")
st.title("🌸 Iris Flower Classification App")

# -----------------------------
# Load Data & Train Model
# -----------------------------
X, y, feature_names, target_names = load_data()
X_train, X_test, y_train, y_test = split_data(X, y)

model = train_model(X_train, y_train)
accuracy, cm, report = evaluate_model(model, X_test, y_test)

# -----------------------------
# Inputs
# -----------------------------
st.subheader("Enter Flower Measurements")

sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.1)
sepal_width  = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.5)
petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 1.4)
petal_width  = st.slider("Petal Width (cm)", 0.1, 2.5, 0.2)

# -----------------------------
# Prediction
# -----------------------------
if st.button("🔍 Predict"):
    prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
    st.success(f"🌼 Predicted Species: **{target_names[prediction[0]].upper()}**")

# -----------------------------
# Model Performance
# -----------------------------
st.markdown("---")
st.subheader("📊 Model Accuracy")
st.write(accuracy)
