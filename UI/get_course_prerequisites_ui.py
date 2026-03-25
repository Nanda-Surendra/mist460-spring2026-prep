import streamlit as st
from fetch_data import fetch_data

def get_course_prerequisites_ui():

    subject_code = st.text_input("Enter Subject Code *")  # * indicates required
    course_number = st.text_input("Enter Course Number (optional)")
    
    if st.button("Fetch Course Prerequisites"):
        params = {}
        if subject_code.strip():
            params["subject_code"] = subject_code.strip()
        if course_number.strip():
            params["course_number"] = course_number.strip()
        
        df = fetch_data("get_course_prerequisites", params)

        if df is not None and not df.empty:
            st.dataframe(df, use_container_width=True, hide_index=True)
        else:
            st.info("No course prerequisites found for the specified subject code.")