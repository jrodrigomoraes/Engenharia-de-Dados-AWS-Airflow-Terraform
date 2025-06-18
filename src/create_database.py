import psycopg2

# Conexão ao banco default 'postgres' da instância RDS
conn = psycopg2.connect(
    dbname='postgres',
    user='postgres',
    password='neutron123',
    host='locadora-db.c2t602m2ee37.us-east-1.rds.amazonaws.com',
    port='5432'
)

conn.autocommit = True
cursor = conn.cursor()

# Criar o banco de dados 'locadora'
try:
    cursor.execute("CREATE DATABASE locadora;")
    print("Banco de dados 'locadora' criado com sucesso!")
except Exception as e:
    print("Erro ao criar banco:", e)

cursor.close()
conn.close()
