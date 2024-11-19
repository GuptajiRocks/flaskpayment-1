import pyodbc
import os
from dotenv import load_dotenv
load_dotenv()

server = 'arihantsqldbs.database.windows.net'
database = 'freeDB'
username = 'arihant'
password = os.environ["SQLPSWD"]
driver= '{ODBC Driver 18 for SQL Server}'

with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT TOP 3 name, collation_name FROM sys.databases")
        row = cursor.fetchone()
        while row:
            print (str(row[0]) + " " + str(row[1]))
            row = cursor.fetchone()