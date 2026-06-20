import streamlit as st
import joblib
model = joblib.load("model.pkl")
st.title("Clinical Dashboard")

st.set_page_config(page_title="Clinical Input Dashboard", layout="wide")

st.title("🩺 Doctor Clinical Input Dashboard")
st.header("👤 Patient Information")

sex = st.selectbox("Sex", ["Male", "Female", "Other"])
age = st.slider("Age", 0, 120, 30)

weight = st.number_input("Weight (kg)", 0.0, 200.0, 70.0)
height = st.number_input("Height (cm)", 50.0, 220.0, 170.0)

st.header("💓 Blood Pressure")

bp_category = st.selectbox(
    "Blood Pressure Category",
    ["Normal", "Elevated", "Stage 1 Hypertension", "Stage 2 Hypertension"]
)

sys_bp = st.slider("Systolic BP", 80, 250, 120)
dia_bp = st.slider("Diastolic BP", 40, 150, 80)

st.header("🧪 Lab Results")

chol = st.slider("Total Cholesterol (mg/dL)", 100, 500, 200)
hdl = st.slider("HDL (mg/dL)", 20, 100, 50)
ldl = st.slider("LDL (mg/dL)", 50, 300, 120)
glucose = st.slider("Fasting Blood Sugar (mg/dL)", 50, 300, 100)

st.header("🧍 Lifestyle Factors")

smoking = st.selectbox("Smoking Status", ["No", "Yes"])
diabetes = st.selectbox("Diabetes Status", ["No", "Yes"])
activity = st.selectbox("Physical Activity Level", ["Low", "Moderate", "High"])
family_history = st.selectbox("Family History of CVD", ["No", "Yes"])

st.header("📊 Clinical Output")

if st.button("Generate Report"):

    st.subheader("📋 Patient Summary")

    st.write("Sex:", sex)
    st.write("Age:", age)
    st.write("Weight:", weight)
    st.write("Height:", height)

    st.write("BP Category:", bp_category)
    st.write("BP:", sys_bp, "/", dia_bp)

    st.write("Cholesterol:", chol)
    st.write("HDL:", hdl)
    st.write("LDL:", ldl)
    st.write("Glucose:", glucose)

    st.write("Smoking:", smoking)
    st.write("Diabetes:", diabetes)
    st.write("Activity:", activity)
    st.write("Family History:", family_history)

    
