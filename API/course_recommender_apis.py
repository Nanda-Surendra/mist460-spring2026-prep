import fastapi
from get_course_sections_for_specified_course import get_course_sections_for_specified_course
from get_course_prerequisites import get_course_prerequisites
from validate_user import validate_user
from has_student_met_prerequisites_for_course import has_student_met_prerequisites_for_course
from get_course_recommendations_for_job import get_course_recommendations_for_job
from get_all_jobs import get_all_jobs

app = fastapi.FastAPI()

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

@app.get("/get_course_recommendations_for_job")
def get_course_recommendations_for_job_endpoint(
    jobDescription: str
):
    return get_course_recommendations_for_job(jobDescription)

@app.get("/get_all_jobs")
def get_all_jobs_endpoint():
    return get_all_jobs()