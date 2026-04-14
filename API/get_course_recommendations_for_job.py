import os
import json
import pprint
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from get_db_connection import get_db_connection

load_dotenv()

def get_course_recommendations_for_job(job_description: str) -> str:

    embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")
    chat_llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    semester_name = "Spring"
    year_value = 2026

    user_query = f"Suggest courses that are a good fit for a job with the description: {job_description} offered in {semester_name} {year_value}."

    # Create embedding for the job description to run semantic search
    query_embedding = embedding_model.embed_query(job_description)

    print("\nUser Query Embedding:")
    pprint.pprint(query_embedding)

    connection = get_db_connection()
    cursor = connection.cursor(as_dict=True)

    cursor.execute(
        "EXEC procGetCourseRecommendationsForJob %s, %s, %s",
        (json.dumps(query_embedding), semester_name, year_value)
    )

    semantic_results = cursor.fetchall()

    cursor.close()
    connection.close()

    pprint.print(semantic_results)

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            """
            You are an expert academic advisor. Your task is to analyze the provided course data
            and suggest the best recommended courses based on a user's query.

            Guidelines:
            - Use only the provided context. Do not make up information.
            - Summarize why each course is a good fit, citing specific evidence from the course description.
            - Present results in a clear, professional format.
            """
        ),
        (
            "human",
            """
            User Query:
            {user_query}

            Retrieved Context:
            {context}

            Please provide your course recommendations.
            """
        ),
    ])

    chain = prompt | chat_llm
    response = chain.invoke({
        "user_query": user_query,
        "context":    semantic_results
    })

    return response.content