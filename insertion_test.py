import csv
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
#criar database
conn = psycopg2.connect(dbname='test_insert', user='postgres', password='thalita', port=5432)

conn.autocommit = True
cursor = conn.cursor()
#criar table
# criar_table = '''CREATE TABLE PARTIDO(id varchar(5) NOT NULL PRIMARY KEY,\
# siglaPartido varchar(20));'''
  
# cursor.execute(criar_table)


#inserir arquivo
# cursor.copy_from(open('C:\\Users\\thali\\OneDrive\\Área de Trabalho\\db_manipulation\\partidos.csv',"r"),table="partido",sep=",")
  
select_cont = '''select * from partido;'''
cursor.execute(select_cont)
for i in cursor.fetchall():
    print(i)
  
conn.commit()
conn.close()