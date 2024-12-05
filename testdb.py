import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

server = 'arihantsqldbs.database.windows.net'
database = 'freeDB'
username = 'arihant'
password = os.getenv("SQLPSWD")
driver= '{ODBC Driver 18 for SQL Server}'

conn = pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
curs = conn.cursor()

curs.execute("SELECT name, database_id, create_date FROM sys.databases;")
res = curs.fetchall()
print(res)