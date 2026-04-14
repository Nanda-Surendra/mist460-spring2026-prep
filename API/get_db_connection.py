import pymssql
import os
from dotenv import load_dotenv

load_dotenv()

# def get_db_connection():
#     server = "localhost"
#     database = "MIST460_RDB_Prep"
    
#     connection_string = (
#         f"DRIVER={{ODBC Driver 18 for SQL Server}};"
#         f"SERVER={server};"
#         f"DATABASE={database};"
#         f"Trusted_Connection=yes;"
#         f"Encrypt=yes;"
#         f"TrustServerCertificate=yes;"
#         f"Connection Timeout=30;"
#     )
#     return pyodbc.connect(connection_string)

def get_db_connection():

    server = os.getenv('DB_SERVER')
    database = os.getenv('DB_NAME')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    #driver = os.getenv('DB_DRIVER')

    #connection_string = f"DRIVER={driver};SERVER={server}; DATABASE={database};UID={user};PWD={password};Encrypt=yes;TrustServerCertificate=yes;Connection Timeout=30;"

    #connection_string = f"DRIVER={driver};SERVER={server}; DATABASE={database};UID={user};PWD={password};"
    #connection_string += f"Encrypt=yes;TrustServerCertificate=yes;Connection Timeout=30;"

    #return pyodbc.connect(connection_string)
    return pymssql.connect(server=server, user=user, password=password, database=database, port =1433, tds_version='7.4')


    
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
    
