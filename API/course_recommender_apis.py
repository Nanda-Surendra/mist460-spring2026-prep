from fastapi import FastAPI
from get_course_sections_for_specified_course import get_course_sections_for_specified_course
from get_course_prerequisites import get_course_prerequisites
from validate_user import validate_user
from has_student_met_prerequisites_for_course import has_student_met_prerequisites_for_course

app = FastAPI()

@app.get("/get_course_sections_for_specified_course")
def get_course_sections_endpoint(
    subjectCode: str = None,
    courseNumber: str = None
):
    return get_course_sections_for_specified_course(subjectCode, courseNumber)

@app.get("/get_course_prerequisites")
def get_course_prerequisites_endpoint(
    subjectCode: str = None,
    courseNumber: str = None
):
    return get_course_prerequisites(subjectCode, courseNumber)

@app.get("/validate_user")
def validate_user_endpoint(
    username: str,
    password: str
):
    return validate_user(username, password)

@app.get("/has_student_met_prerequisites_for_course")
def has_student_met_prerequisites_for_course_endpoint(
    studentID: int,
    subjectCode: str,
    courseNumber: str
):
    return has_student_met_prerequisites_for_course(studentID, subjectCode, courseNumber)
