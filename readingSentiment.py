import sqlite3
import pandas as pd

conn = sqlite3.connect('twitter.db')
c = conn.cursor()

df = pd.read_sql("SELECT * FROM sentiment WHERE tweet LIKE '%trump%' ORDER BY unix DESC LIMIT 1000", conn)
print(df.tail())
