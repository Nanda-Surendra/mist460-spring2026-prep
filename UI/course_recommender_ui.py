import pandas as pd
import streamlit as st
import requests

FASTAPI_URL = "http://localhost:8000"

def fetch_data(endpoint : str, params : dict, method: str = "get") -> pd.DataFrame:
    if method == "get":
        response = requests.get(f"{FASTAPI_URL}/{endpoint}", params=params)

    if response.status_code == 200:
        payload = response.json()
        rows = payload.get("data", [])
        df = pd.DataFrame(rows)
        return df

    else:
        st.error(f"Error fetching data: {response.status_code}")
        return None

## Create a sidebar with a dropdown for the course recommender functionalities
with st.sidebar:
    st.title("Course Recommender System")

    #Dropdown for course recommender functionalities
    api_end_point = st.selectbox("Select Functionality", ["Get Course Sections for Specified Course", "Get Course Prerequisites"])
    if api_end_point == "Get Course Sections for Specified Course":
        subject_code = st.text_input("Enter Subject Code (e.g., CS, MATH)")
        course_number = st.text_input("Enter Course Number (e.g., 101, 201)")
        if st.button("Fetch Course Sections"):
            params = {"subjectCode": subject_code, "courseNumber": course_number}
            df = fetch_data("get_course_sections_for_specified_course/", params)
            if df is not None:
                st.dataframe(df)
            else:
                st.info("No course sections found for the specified course.")

    elif api_end_point == "Get Course Prerequisites":
        subject_code = st.text_input("Enter Subject Code (e.g., CS, MATH)")
        course_number = st.text_input("Enter Course Number (e.g., 101, 201)")
        if st.button("Fetch Course Prerequisites"):
            params = {"subjectCode": subject_code, "courseNumber": course_number}
            df = fetch_data("get_course_prerequisites/", params)
            if df is not None:
                st.dataframe(df)
            else:
                st.info("No course prerequisites found for the specified course.")
