import sqlite3
import pandas as pd
conn = sqlite3.connect("/home/zxf/zz1806/zz1806/untitled6/db.sqlite3")
# huabans = pd.read_sql("select * from huaban",conn)
cursor=conn.cursor()
cursor.execute("")
Tables=cursor.fetchall()

