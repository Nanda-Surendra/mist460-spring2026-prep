import streamlit as st
from fetch_data import fetch_data

def has_student_met_prerequisites_for_course_ui():
    
    st.header("Has Student Taken All Prerequisites For a Course?")
    student_id = st.number_input("Student ID", value=st.session_state.app_user_id, disabled=True)
    subject_code = st.text_input("Subject Code")
    course_number = st.text_input("Course Number")
    if st.button("Check Prerequisites"):
        df = fetch_data(
            "check_if_student_has_taken_all_prerequisites_for_course/",
            {"studentID": student_id, "subjectCode": subject_code, "courseNumber": course_number}
        )
        if df is not None:
            if df.empty:
                st.success("The student has taken all prerequisites for the specified course.")
            else:
                st.warning("The student has NOT taken all prerequisites for the specified course. Missing prerequisites:")
                st.dataframe(df, use_container_width=True, hide_index=True)
        else:
            st.error("Error checking prerequisites.")