import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Prediction of disease outbreaks", page_icon="🧊", layout="wide")

working_dir = os.path.dirname(os.path.abspath(__file__))

diabetes_model = pickle.load(open(os.path.join(working_dir, 'models/diabetes_model.sav'), 'rb'))
heart_model = pickle.load(open(os.path.join(working_dir, 'models/heart-disease-model.sav'), 'rb'))
parkinsons_model = pickle.load(open(os.path.join(working_dir, 'models/parkinsons-disease-model.sav'), 'rb'))

with st.sidebar:
    selected = option_menu("Select a disease", ["Diabetes", "Heart", "Parkinson's"],
    menu_icon="hospital_fill",
    icons=["activity", "heart", "person"],
    default_index=0)

if selected == "Diabetes":
    st.title("Diabetes Disease Prediction")
    col1,col2,col3 = st.columns(3)
    with col1:
        pregnancies = st.text_input("Pregnancies")
    with col2:
        glucose = st.text_input("Glucose")
    with col3:
        blood_pressure = st.text_input("Blood Pressure")
    with col1:
        skin_thickness = st.text_input("Skin Thickness")
    with col2:
        insulin = st.text_input("Insulin")
    with col3:
        bmi = st.text_input("BMI")
    with col1:
        diabetes_pedigree_function = st.text_input("Diabetes Pedigree Function Value")
    with col2:
        age = st.number_input("Age of the pereson")

    diab_diagnosis = ''

    if st.button("Diabetic Test Result"):
        user_input = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 0:
            diab_diagnosis = "The person is not diabetic"
        else:
            diab_diagnosis = "The person is diabetic"

    st.success(diab_diagnosis)

# Heart Disease Prediction
if selected == "Heart":
    st.title("Heart Disease Prediction")
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input("Age")
        sex = st.text_input("Sex")
        chest_pain_type = st.text_input("Chest Pain Type")
        resting_bp = st.text_input("Resting Blood Pressure")
        exercise_induced_angina = st.text_input("Exercise Induced Angina")
    with col2:
        cholesterol = st.text_input("Cholesterol in mg/dl")
        fasting_blood_sugar = st.text_input("Fasting Blood Sugar")
        rest_ecg = st.text_input("Resting Electrocardiograph Result")
        max_heart_rate = st.text_input("Maximum Heart Rate Achieved")
    with col3:
        oldpeak = st.text_input("ST Depression Induced by Exercise")
        slope= st.text_input("Slope of the Peak Exercise ST Segment")
        major_vessels = st.text_input("No of Vessels Colored by Fluoroscopy")
        thalassemia = st.text_input("Thalassemia")

    heart_diagnosis = ''

    if st.button("Heart Disease Test Result"):
        user_input = [age, sex, chest_pain_type, resting_bp, exercise_induced_angina, cholesterol, fasting_blood_sugar, rest_ecg, max_heart_rate, oldpeak, slope, major_vessels, thalassemia]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_model.predict([user_input])

        if heart_prediction[0] == 0:
            heart_diagnosis = "The person does not have a heart disease"
        else:
            heart_diagnosis = "The person has heart disease"

    st.success(heart_diagnosis)


# Parkinson's Disease Prediction
if selected == "Parkinson's":
        st.title("Parkinson's Disease Prediction")
        col1, col2, col3 = st.columns(3)
        with col1:
            mdvp_fo = st.text_input("MDVP:Fo(Hz)")
            mdvp_fhi = st.text_input("MDVP:Fhi(Hz)")
            mdvp_flo = st.text_input("MDVP:Flo(Hz)")
            jitter_percent = st.text_input("Jitter(%)")
            jitter_abs = st.text_input("Jitter(Abs)")
            rap = st.text_input("RAP")
            ppq = st.text_input("PPQ")
            ddp = st.text_input("DDP")
        with col2:
            shimmer = st.text_input("Shimmer")
            shimmer_db = st.text_input("Shimmer(dB)")
            apq3 = st.text_input("APQ3")
            apq5 = st.text_input("APQ5")
            apq = st.text_input("APQ")
            dda = st.text_input("DDA")
            nhr = st.text_input("NHR")
            hnr = st.text_input("HNR")
        with col3:
            rpde = st.text_input("RPDE")
            dfa = st.text_input("DFA")
            spread1 = st.text_input("spread1")
            spread2 = st.text_input("spread2")
            d2 = st.text_input("D2")
            ppe = st.text_input("PPE")

        parkinsons_diagnosis = ''

        if st.button("Parkinson's Disease Test Result"):
            user_input = [mdvp_fo, mdvp_fhi, mdvp_flo, jitter_percent, jitter_abs, rap, ppq, ddp, shimmer, shimmer_db, apq3, apq5, apq, dda, nhr, hnr, rpde, dfa, spread1, spread2, d2, ppe]

            user_input = [float(x) for x in user_input]

            parkinsons_prediction = parkinsons_model.predict([user_input])

            if parkinsons_prediction[0] == 0:
                parkinsons_diagnosis = "The person does not have Parkinson's disease"
            else:
                parkinsons_diagnosis = "The person has Parkinson's disease"

        st.success(parkinsons_diagnosis)