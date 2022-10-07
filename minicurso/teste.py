import psycopg2

# estabelece a conexao com o postgres
conn = psycopg2.connect(host='localhost', user="postgres", password="postgres", port=5432)

# faz a confirmacao de cada execucao automaticamente
conn.autocommit = True

# permite que o python execute o comando em SQL no BD
cursor = conn.cursor()

nome_db = 'camera'

cursor.execute('CREATE DATABASE ' + nome_db)

conn -