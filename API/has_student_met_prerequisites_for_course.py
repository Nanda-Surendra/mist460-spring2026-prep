#has_student_met_prerequisites_for_course

from get_db_connection import get_db_connection

def has_student_met_prerequisites_for_course(
    studentID: int,
    subjectCode: str,
    courseNumber: str
):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Execute the stored procedure
    cursor.execute("{call procCheckIfStudentHasMetPrerequisitesForCourse(?, ?, ?)}", studentID, subjectCode, courseNumber)

    # Fetch results
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    # Convert to list of dicts
    results = [
        {"SubjectCode": row.SubjectCode, "CourseNumber": row.CourseNumber, "MinimumGradeRequired": row.MinimumGradeRequired, "StudentGrade": row.StudentGrade}
        for row in rows
    ]
    return {"data": results}
