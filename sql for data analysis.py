import pyodbc as odbc
import pandas as pd

DRIVER_NAME = 'ODBC Driver 18 for SQL Server'
SERVER_NAME = 'Aahil\SQLEXPRESS'
DATABASE_NAME = 'CollegeDB'

print(odbc.drivers())

conn_string = f"""
DRIVER={{{DRIVER_NAME}}};
SERVER={SERVER_NAME};
DATABASE={DATABASE_NAME};
Trusted_Connection=yes;
Encrypt=no;
"""

conn = odbc.connect(conn_string)
#print(conn)
query = "SELECT * FROM Courses" 

cursor = conn.cursor()
cursor.execute(query)

results = cursor.fetchall()

for row in results:
    print(row)

try:
    df = pd.read_sql_query("SELECT * FROM Staff", conn)
    print(df.head())  
except Exception as e:
    print("Error:", e)

df.head()
cursor.close()
conn.close()