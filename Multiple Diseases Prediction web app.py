# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 17:03:20 2026

@author: arsla
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the models

heart_diseases_model = pickle.load(open("heart_diseases_model.sav" , "rb"))

parkinsons_model = pickle.load(open("parkinsons_model.sav" , "rb"))

diabetes_model = pickle.load(open("diabetes_model.sav" , "rb"))

breast_cancer_model = pickle.load(open("breast_cancer_model.sav" , "rb"))


# Sidebar for navigation

with st.sidebar:
    selected = option_menu('Multiple Diseases Prediction System',
                           ['Diabetes Prediction', 
                            'Heart Diseases Prediction',
                            'Parkinsons Prediction',
                            'Breast Cancer Prediction'],
                           icons=['activity' , 'heart-pulse-fill' ,
                                  'person' , 'bookmarks'],
                            default_index=0)
    
    
# Diabetes Prediction page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction Model')
    
    # Input data from the user
    # data in columns
    col1 , col2 , col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input("No.of Pregnancies")
    
    with col2:
        Glucose = st.text_input("Sugar (or Glucose) level")
    
    with col3:
        BloodPressure = st.text_input("BloodPressure level")
    
    with col1:
        SkinThickness = st.text_input("Skin Thickness")
    
    with col2:
        Insulin = st.text_input("Insulin level")
    
    with col3:
        BMI = st.text_input("BMI value")
    
    with col1:
        DiabetesPedigreeFunction = st.text_input("DiabetesPedigreeFunction level")
    
    with col2:
        Age = st.text_input("Age")
    
    # Code for prediction
    diabetes_diagnosis = ''
    
    # Button for prediction
    user_input_diab = [Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]
    if st.button('Diabetes Test Result'):
        if '' in user_input_diab:
            st.error('Please fill all the fields')
        else:
            diabetes_prediction = diabetes_model.predict([user_input_diab])
            
            if (diabetes_prediction[0] == 1):
                diabetes_diagnosis = 'The person is Diabetic'
            else:
                diabetes_diagnosis = 'The person is not-Diabetic'
            
    st.success(diabetes_diagnosis)
    


# Heart Diseases Prediction page
if (selected == 'Heart Diseases Prediction'):
    
    # page title
    st.title('Heart Diseases Prediction Model')
    
    # Input data from the user
    col1 , col2  = st.columns(2)
    
    with col1:
        age = st.number_input('Age')
    
    with col2:
        sex = st.number_input('Gender')
    
    with col1:
        cp = st.number_input('Chest Pain Type')
        
    with col2:
        trestbps = st.number_input('Resting BloodPressure')
    
    with col1:
        chol = st.number_input('Serum Cholesterol in mg/dl')
    
    with col2:
        fbs = st.number_input('Fasting Blood-sugar > 120 mg/dl')
        
    with col1:
        restecg = st.number_input('Resting Electrocardiographic results (values 0,1,2)')
    
    with col2:
        thalach = st.number_input('Maximum Heart-rate achieved')
    
    with col1:
        exang = st.number_input('Exercise Induced Angina')
    
    with col2:
        oldpeak = st.number_input('oldpeak = ST depression induced by exercise relative to rest')
    
    with col1:
        slope = st.number_input('the slope of the peak exercise ST segment')
    
    with col2:
        ca = st.number_input('number of major vessels (0-3) colored by flourosopy')
        
    with col1:
        thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
    
    # Code for prediction
    heart_diagnosis = ''
    
    # Button for prediction
    user_input_heart = [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
    
    if st.button('Heart Diseases Test Result'):
        if '' in user_input_heart:
            st.error('Please fill all the fields')
        else:
            heart_prediction = heart_diseases_model.predict([user_input_heart])
            
            if (heart_prediction[0] == 1):
                diabetes_diagnosis = 'Patient is suffering from Heart diseases ,Consult with heart specialist...!'
            else:
                heart_diagnosis = 'The Person does not have a Heart Disease.You have completely Healthy Heart!'
            
    st.success(heart_diagnosis)
    

# Parkinsons Prediction page
if (selected == 'Parkinsons Prediction'):
    
    # page title
    st.title('Parkinsons Prediction Model')
    
    # Input data from the user
    MDVP_Fo_Hz = st.number_input(' Average vocal fundamental frequency')
    
    MDVP_Fhi_Hz = st.number_input('Maximum vocal fundamental frequency')
    
    MDVP_Flo_Hz = st.number_input('Minimum vocal fundamental frequency')
    
    MDVP_Jitter = st.number_input('MDVP:Jitter(%)')
    
    MDVP_Jitter_abs = st.number_input('MDVP:Jitter(abs)')
    
    MDVP_RAP = st.number_input('MDVP:RAP')
    
    MDVP_PPQ = st.number_input('MDVP:PPQ')
    
    Jitter_DDP = st.number_input('Jitter:DDP')
    
    MDVP_shimmer = st.number_input('MDVP:shimmer')
    
    MDVP_shimmer_db = st.number_input('MDVP_shimmer(db)')
    
    Shimmer_APQ3 = st.number_input('Shimmer:APQ3')
    
    Shimmer_APQ5 = st.number_input('Shimmer:APQ5')
    
    MDVP_APQ = st.number_input('MDVP:APQ')
    
    Shimmer_DDA = st.number_input('Shimmer_DDA')
    
    NHR = st.number_input('NHR')
    
    HNR = st.number_input('HNR')
    
    RPDE = st.number_input('RPDE')
    
    DFA = st.number_input('DFA')
    
    spread1 = st.number_input('spread1')
    
    spread2 = st.number_input('spread2')
    
    D2 = st.number_input('D2')
    
    PPE = st.number_input('PPE')
    
    # Code for prediction
    parkinsons_diagnosis = ''
    
    # Button for prediction
    user_input_park = [MDVP_Fo_Hz,MDVP_Fhi_Hz,MDVP_Flo_Hz,MDVP_Jitter,MDVP_Jitter_abs,MDVP_RAP,MDVP_PPQ,Jitter_DDP,MDVP_shimmer,MDVP_shimmer_db,Shimmer_APQ3,Shimmer_APQ5,MDVP_APQ,Shimmer_DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]
    
    if st.button('Parkinsons Diseases Test Result'):
        if '' in user_input_park:
            st.error('Please fill all the fields')
        else:
            parkinsons_prediction = parkinsons_model.predict([user_input_park])
            
            if (parkinsons_prediction[0] == 1):
                parkinsons_diagnosis = 'Person has parkinsons diseases'
            else:
                parkinsons_diagnosis = 'The Person is healthy'
            
    st.success(parkinsons_diagnosis)
    
    
    
    
# Breast Cancer Prediction page
if (selected == 'Breast Cancer Prediction'):
    
    # page title
    st.title('Breast Cancer Prediction Model')
    
    # Input data from user
    radius_mean = st.number_input('radius_mean')
    
    texture_mean = st.number_input('texture_mean')
    
    perimeter_mean = st.number_input('perimeter_mean')
    
    area_mean = st.number_input('area_mean')
    
    smoothness_mean = st.number_input('smoothness_mean')
    
    compactness_mean = st.number_input('compactness_mean')
    
    concavity_mean = st.number_input('concavity_mean')
    
    concave_points_mean = st.number_input('concave points_mean')
    
    symmetry_mean = st.number_input('symmetry_mean')
    
    fractal_dimension_mean = st.number_input('fractal_dimension_mean')
    
    radius_se = st.number_input('radius_se')
    
    texture_se = st.number_input('texture_se')
    
    perimeter_se = st.number_input('perimeter_se')
    
    area_se = st.number_input('area_se')
    
    smoothness_se = st.number_input('smoothness_se')
    
    compactness_se = st.number_input('compactness_se')
    
    concavity_se = st.number_input('concavity_se')
    
    concave_points_se = st.number_input('concave points_se')
    
    symmetry_se = st.number_input('symmetry_se')
    
    fractal_dimension_se = st.number_input('fractal_dimension_se')
    
    radius_worst = st.number_input('radius_worst')
    
    texture_worst = st.number_input('texture_worst')
    
    perimeter_worst = st.number_input('perimeter_worst')
    
    area_worst = st.number_input('area_worst')
    
    smoothness_worst = st.number_input('smoothness_worst')
    
    compactness_worst = st.number_input('compactness_worst')
    
    concavity_worst = st.number_input('concavity_worst')
    
    concave_points_worst = st.number_input('concave points_worst')
    
    symmetry_worst = st.number_input('symmetry_worst')
    
    fractal_dimension_worst = st.number_input('fractal_dimension_worst')
    
    # Code for prediction
    cancer_diagnosis = ''
    
    # Button for prediction
    user_input_cancer = [radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean,compactness_mean,concavity_mean,concave_points_mean,symmetry_mean,fractal_dimension_mean,radius_se,texture_se,perimeter_se,area_se,smoothness_se,compactness_se,concavity_se,concave_points_se,symmetry_se,fractal_dimension_se,radius_worst,texture_worst,perimeter_worst,area_worst,smoothness_worst,compactness_worst,concavity_worst,concave_points_worst,symmetry_worst,fractal_dimension_worst]
    
    if st.button('Breast Cancer Prediction Test Result'):
        if '' in user_input_cancer:
            st.error('Please fill all the fields')
        else:
            cancer_prediction = breast_cancer_model.predict([user_input_cancer])
            
            if (cancer_prediction[0] == 0):
                cancer_diagnosis = 'The tumor is Malignant (cancerous).'
            else:
                cancer_diagnosis = 'The tumor is Benign (non-cancerous)'
            
    st.success(cancer_diagnosis)


