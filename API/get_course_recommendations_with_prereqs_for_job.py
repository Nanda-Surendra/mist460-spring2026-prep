import os
import json
import pprint
import pymssql
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from get_db_connection import get_db_connection

load_dotenv()


def get_course_recommendations_for_job(job_description: str) -> str:

    openai_api_key = os.getenv("OPENAI_API_KEY")

    embedding_model = OpenAIEmbeddings(
        model="text-embedding-3-small",
        openai_api_key=openai_api_key
    )

    chat_llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0,
        openai_api_key=openai_api_key
    )

    semester_name = "Spring"
    year_value = 2026

    user_query = f"Suggest courses that are a good fit for a job with the description: {job_description} offered in {semester_name} {year_value}."

    # Create embedding for the job description to run semantic search
    query_embedding = embedding_model.embed_query(job_description)

    print("\nUser Query Embedding:")
    pprint.pprint(query_embedding)

    connection = get_db_connection()
    cursor = connection.cursor(as_dict=True)

    # Semantic similarity search using VECTOR_DISTANCE
    # Join Chunks -> Course -> CourseOffering -> Prerequisites
    cursor.execute("""
        SELECT TOP 5
            c.CourseID,
            c.Title          AS courseTitle,
            c.SubjectCode    AS subjectCode,
            c.CourseNumber   AS courseNumber,
            c.CourseDescription AS courseDescription,
            co.Semester      AS semester,
            co.Year          AS year,
            co.CourseOfferingID AS courseOfferingID,
            ch.content       AS evidence,
            VECTOR_DISTANCE('cosine', ch.embedding, CAST(%s AS VECTOR(1536))) AS distance
        FROM Chunks ch
        JOIN Course c ON ch.CourseID = c.CourseID
        JOIN CourseOffering co ON c.CourseID = co.CourseID
        WHERE co.Semester = %s AND co.Year = %s
        ORDER BY distance ASC
    """, (json.dumps(query_embedding), semester_name, year_value))

    top_chunks = cursor.fetchall()

    # For each result, fetch prerequisites separately
    semantic_results = []
    for row in top_chunks:
        cursor.execute("""
            SELECT 
                p.CourseID       AS courseID,
                p.Title          AS courseTitle,
                p.SubjectCode    AS subjectCode,
                p.CourseNumber   AS courseNumber,
                p.CourseDescription AS description
            FROM CoursePrerequisite cp
            JOIN Course p ON cp.PrerequisiteCourseID = p.CourseID
            WHERE cp.CourseID = %s
        """, (row["CourseID"],))

        prerequisites = cursor.fetchall()

        semantic_results.append({
            "courseID":         row["CourseID"],
            "courseTitle":      row["courseTitle"],
            "subjectCode":      row["subjectCode"],
            "courseNumber":     row["courseNumber"],
            "courseDescription": row["courseDescription"],
            "semester":         row["semester"],
            "year":             row["year"],
            "courseOfferingID": row["courseOfferingID"],
            "distance":         row["distance"],
            "evidence":         row["evidence"],
            "prerequisites":    prerequisites if prerequisites else []
        })

    cursor.close()
    connection.close()

    pprint.pprint(semantic_results)

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            """
            You are an expert academic advisor. Your task is to analyze the provided course data
            and suggest the best recommended courses based on a user's query.

            Guidelines:
            - Use only the provided context. Do not make up information.
            - Summarize why each course is a good fit, citing specific evidence from the course description.
            - Consider any listed prerequisites when making recommendations.
            - For each recommended course, provide an enrollment link using this format:
              http://localhost:8000/enroll_student_in_course_offering/?studentID={student_id}&courseOfferingID={{courseOfferingID}}
              Replace {{courseOfferingID}} with the actual CourseOfferingID from the context.
            - Present results in a clear, professional format with clickable links.
            """
        ),
        (
            "human",
            """
            User Query:
            {user_query}

            Retrieved Context:
            {context}

            Please provide your course recommendations with enrollment links.
            """
        ),
    ])

    chain = prompt | chat_llm
    response = chain.invoke({
        "user_query": user_query,
        "context":    semantic_results
    })

    return response.content