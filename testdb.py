import pyodbc
import os
from dotenv import load_dotenv
load_dotenv()

server = 'arihantsqldbs.database.windows.net'
database = 'freeDB'
username = 'arihant'
password = os.environ["SQLPSWD"]
driver= '{ODBC Driver 18 for SQL Server}'

conn = pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
curs = conn.cursor()

curs.execute("SELECT name FROM master.dbo.sysdatabases")
res = curs.fetchall()
print(res)