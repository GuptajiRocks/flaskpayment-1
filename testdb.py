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

curs.execute("use freeDB;")
curs.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES;")
# curs.execute("""CREATE TABLE [dbo].[Customers] (
#     [CustomerID] INT PRIMARY KEY IDENTITY(1,1),
#     [FirstName] NVARCHAR(50) NOT NULL,
#     [LastName] NVARCHAR(50) NOT NULL,
#     [Email] NVARCHAR(100) UNIQUE,
#     [Phone] NVARCHAR(20)
# );""")

res = curs.fetchall()
print(res)