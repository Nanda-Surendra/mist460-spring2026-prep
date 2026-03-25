import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    server = os.getenv("DB_SERVER")
    database = os.getenv("DB_NAME")
    username = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    #ODBC Driver 18 for SQL Server can ONLY be used in Synchronous mode
    connection_string = f"DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};Encrypt=yes;TrustServerCertificate=yes;Connection Timeout=30;"
    return pyodbc.connect(connection_string)

    
    """ connection_string = (
        f'DRIVER={DB_DRIVER};'
        f'SERVER={DB_SERVER};'
        f'DATABASE={DB_DATABASE};'
        f'UID={DB_LOGIN};'
        f'PWD={DB_PASSWORD};'
        'TrustServerCertificate=yes;'
        'Connection Timeout=30;'
        'Encrypt=yes;'
    )
    return pyodbc.connect(connection_string)
 """