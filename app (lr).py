import pandas as pd
import numpy as np
import streamlit as st
import pickle

with open("LinearRegression_CarPrice (1).pkl","rb") as file:
    model=pickle.load(file)


st.title("CAR PRICE PREDICTOR")

#input fields
name=st.text_input("select name of a car :")
company=st.text_input("select company of a car :")
year=st.number_input("year of manufacturing" , min_value=1990 , max_value= 2024 , step=2)
kms_driven=st.number_input("Enter kms", min_value=0 , value=00)
fuel_type=st.selectbox("feul of a car",options=['Petrol','Diesel','LPG'])

user_input=pd.DataFrame([[name,company,year,kms_driven,fuel_type]] ,columns=['name','company', 'year', 'kms_driven' , 'fuel_type'] )

if st.button("PREDICT:"):
    
    predicted=model.predict(user_input)[0]

    st.success(f"Predicted Car Price Is :{predicted}")


#streamlit run "app (lr).py"

