from sqlalchemy import create_engine
import psycopg2

engine = create_engine('postgresql+psycopg2://postgre:D4t4b4s3@localhost:5432/datos_argentina')

conn = engine.connect()

nombres= conn.table_names()
print (nombres)