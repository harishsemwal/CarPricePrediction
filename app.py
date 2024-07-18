import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score

# Set up the page layout
st.set_page_config(page_title="Car Price Prediction", layout="wide")

# Title and description
st.title("Car Price Prediction App")
st.write("This web app predicts the selling price of cars based on various features.")

# Load dataset
@st.cache_data
def load_data():
    url = 'https://raw.githubusercontent.com/nehalbirla/vehicle-dataset-from-cardekho/master/car%20data.csv'
    df = pd.read_csv(url)
    return df
# Single observation prediction
st.subheader("Predict a Single Observation")

Present_Price = st.number_input("Present Price (in Lakhs)", 0.0, 100.0, step=0.1)
Kms_Driven = st.number_input("Kms Driven", 0, 200000, step=1000)
Owner = st.selectbox("Owner", dataset['Owner'].unique())  # Assuming 'Owner' column exists
Years_Old = st.slider("Years Old", 0, 20, step=1)
Fuel_Type_Diesel = st.selectbox("Fuel Type Diesel", [0, 1])
Fuel_Type_Petrol = st.selectbox("Fuel Type Petrol", [0, 1])
Seller_Type_Individual = st.selectbox("Seller Type", dataset['Seller_Type'].unique())  # Assuming 'Seller_Type' column exists
Transmission_Manual = st.selectbox("Transmission", dataset['Transmission'].unique())  # Assuming 'Transmission' column exists

single_obs = pd.DataFrame([[Present_Price, Kms_Driven, Owner, Years_Old, Fuel_Type_Diesel, Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Manual]],
                          columns=x.columns)

selected_model = st.selectbox("Select Model", ["Linear Regression", "Random Forest", "Decision Tree"])

if st.button("Predict"):
    prediction = models[selected_model][0].predict(single_obs)
    st.write(f"Predicted Selling Price: {prediction[0]:.2f} Lakhs")
