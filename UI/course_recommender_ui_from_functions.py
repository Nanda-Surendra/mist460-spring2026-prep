import streamlit as st
from get_course_sections_for_specified_course_ui import get_course_sections_for_specified_course_ui
from get_course_prerequisites_ui import get_course_prerequisites_ui
from validate_user_ui import validate_user_ui

## Create a sidebar with a dropdown for the course recommender functionalities
with st.sidebar:
    st.title("Course Recommender System")

    #Dropdown for course recommender functionalities
    api_end_point = st.selectbox("Select Functionality", 
                                [   "Validate User",
                                    "Get Course Sections for Specified Course", 
                                    "Get Course Prerequisites",
                                    "Has Student Met Prerequisites For Course"]
                                )

if api_end_point == "Validate User":
    validate_user_ui()

elif api_end_point == "Get Course Sections for Specified Course":
    get_course_sections_for_specified_course_ui()

elif api_end_point == "Get Course Prerequisites":
    get_course_prerequisites_ui()

elif api_end_point == "Has Student Met Prerequisites For Course":
    get_course_prerequisites_ui()

elif api_end_point == "Get Recommendations for Job Description":
    get_recommendations_for_job_description_ui()
    #st.header("Course Recommendations for Job")

