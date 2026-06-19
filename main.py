import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(page_title="Clinical Dashboard", layout="wide")

# Title
st.title("🩺 Clinical Dashboard")

# Upload section
st.write("Upload patient CSV file to begin analysis")

uploaded_file = st.file_uploader("Choose CSV file", type=["csv"])

# If file is uploaded
if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.success("File uploaded successfully!")

    # Show data
    st.subheader("📊 Patient Data")
    st.dataframe(df)

    # Basic statistics
    st.subheader("📌 Summary Statistics")
    st.write(df.describe())

    # Column info
    st.subheader("📋 Column Info")
    st.write(df.dtypes)

else:
    st.info("Waiting for file upload...")
