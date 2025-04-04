import pandas as pd
import pyodbc

conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=runwei-sql.database.windows.net,1433;"
    "DATABASE=RunweiOpportunities;"
    "UID=sql-admin;"
    "PWD=Runwei2025;"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
    "Connection Timeout=30;"
)

conn = pyodbc.connect(conn_str)
query = """
SELECT ID, Title, Description, Eligibility, Tags, Industry, AreaOfFocus
FROM dbo.Opportunities
"""
df = pd.read_sql(query, conn)
conn.close()

df.to_csv("opportunities_metadata.csv", index=False)
print("✅ Saved metadata to 'opportunities_metadata.csv'")
