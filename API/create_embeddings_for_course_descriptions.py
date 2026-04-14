import json
from get_db_connection import get_db_connection
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter


def create_embeddings_for_course_descriptions():
    """
    Chunks course description text, generates embeddings, and stores them.
    """
    # Initialize models and splitters
    embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=250, chunk_overlap=20)

    connection = get_db_connection()
    cursor = connection.cursor(as_dict=True)  # Returns rows as dicts

    # Fetch all courses with their descriptions
    cursor.execute("EXEC procGetAllCourseDescriptions")
    course_data = cursor.fetchall()

    for row in course_data:
        course_id = row["CourseID"]
        course_description = row["CourseDescription"]

        # Chunk and embed the course description text
        chunks = text_splitter.split_text(course_description)
        chunk_embeddings = embedding_model.embed_documents(chunks)

        # Insert each chunk and its embedding into the Chunks table
        for i, chunk in enumerate(chunks):
            cursor.execute(
            "EXEC procInsertChunkForCourseDescription %s, %s, %s",
            (course_id, chunk, json.dumps(chunk_embeddings[i]))
    )

        connection.commit()
        print(f"Embedded data for {course_id}.")

    cursor.close()
    connection.close()

    
    # CREATE VECTOR INDEX cannot run inside a transaction
    # Use a separate autocommit connection
    # index_connection = get_db_connection()
    # index_connection.autocommit(True)
    # index_cursor = index_connection.cursor()
    # index_cursor.execute("EXEC procCreateVectorIndexOnChunks")
    # index_cursor.close()
    # index_connection.close()

    print("\nAll chunks have been successfully embedded into SQL Server!")

if __name__ == "__main__":
    create_embeddings_for_course_descriptions()