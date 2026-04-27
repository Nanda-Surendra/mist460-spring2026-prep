import streamlit as st
from fetch_data import fetch_data

def get_recommendations_for_job_description_ui():
    job_title = st.text_area("Enter Job Title *")  # * indicates required

    if st.button("Get Course Recommendations"):
        params = {}
        if job_title.strip():
            params["job_title"] = job_title.strip()

        df = fetch_data("get_course_recommendations_for_job", params)

        if df is not None and not df.empty:
            st.dataframe(df, use_container_width=True, hide_index=True)
        else:
            st.info("No course recommendations found for the specified job title.")
        
        # params = {}
        # if subject_code.strip():
        #     params["subject_code"] = subject_code.strip()
        # if course_number.strip():
        #     params["course_number"] = course_number.strip()
        
        # df = fetch_data("get_course_prerequisites", params)

        # if df is not None and not df.empty:
        #     st.dataframe(df, use_container_width=True, hide_index=True)
        # else:
        #     st.info("No course prerequisites found for the specified subject code.")