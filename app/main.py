import streamlit as st
import requests
from utils import ReportGenerator

st.title("Custom Report Generator")

uploaded_file = st.file_uploader("Upload your data file", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Read the file contents
    file_content = uploaded_file.read()
    
    report_generator = ReportGenerator(file_content)

    if st.button("Generate Report"):
        report = report_generator.generate_report()
        st.write(report)
