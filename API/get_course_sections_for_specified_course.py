from get_db_connection import get_db_connection

def get_course_sections_for_specified_course(
    subject_code: str,
    course_number: str
):
    conn = get_db_connection()

    cursor = conn.cursor()
    cursor.execute("{CALL procGetCourseSectionsForSpecifiedCourse(?, ?)}", subject_code, course_number)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    # Convert rows to a list of dictionaries for better JSON serialization
    results = [
        {
            "SubjectCode": row.SubjectCode,
            "CourseNumber": row.CourseNumber,
            "CourseTitle": row.Title,
            "CRN": row.CRN,
            "Semester": row.SectionSemester,
            "Year": row.SectionYear,
            "SectionID": row.SectionID,
            "RemainingOpenings": row.RemainingOpenings,
            "InstructorName": row.InstructorName
        }
        for row in rows
    ]

    return {"data": results}
