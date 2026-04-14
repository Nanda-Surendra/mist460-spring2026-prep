def create_vector_index(connection, embedding_model):
    """Creates a vector index on the Chunks table for fast similarity search."""
    # Get the embedding dimension from the model
    try:
        course_description_embedding = embedding_model.embed_query("course_description_data")
        vector_dimensions = len(course_description_embedding)
    except Exception as e:
        print(f"Could not determine embedding dimensions. Using default 1536. Error: {e}")
        vector_dimensions = 1536  # Default for OpenAI ada-002

    cursor = connection.cursor()

    # Step 1: Create the Chunks table if it doesn't exist
    create_table_query = f"""
    IF NOT EXISTS (
        SELECT * FROM INFORMATION_SCHEMA.TABLES 
        WHERE TABLE_NAME = 'Chunks'
    )
    BEGIN
        CREATE TABLE Chunks (
            id          INT IDENTITY(1,1) PRIMARY KEY,
            content     NVARCHAR(MAX),
            embedding   VECTOR({vector_dimensions})
        )
    END
    """
    cursor.execute(create_table_query)
    connection.commit()
    print(f"Chunks table ready with VECTOR({vector_dimensions}) column.")

    # Step 2: Create the vector index for cosine similarity search
    create_index_query = """
    IF NOT EXISTS (
        SELECT * FROM sys.indexes 
        WHERE name = 'course_description_chunks' 
        AND object_id = OBJECT_ID('Chunks')
    )
    BEGIN
        CREATE VECTOR INDEX course_description_chunks
        ON Chunks (embedding)
        WITH (METRIC = 'cosine')
    END
    """
    cursor.execute(create_index_query)
    connection.commit()
    print("Vector index on Chunks table created.")

    cursor.close()