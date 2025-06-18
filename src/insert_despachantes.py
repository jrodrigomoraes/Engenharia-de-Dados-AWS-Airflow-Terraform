from faker import Faker
import random
import psycopg2

faker = Faker('pt_BR')
Faker.seed(42)

conn = psycopg2.connect(
    dbname='locadora',
    user='postgres',
    password='neutron123',
    host='locadora-db.c2t602m2ee37.us-east-1.rds.amazonaws.com',
    port='5432'
)
cursor = conn.cursor()

def gerar_despachante():
    return (
        faker.name(),
        random.choice(['Ativo', 'Inativo']),
        random.choice(['SP', 'MG', 'RJ', 'RS'])
    )

for _ in range(10):
    cursor.execute("""
        INSERT INTO despachantes (nome, status, filial)
        VALUES (%s, %s, %s)
    """, gerar_despachante())

conn.commit()
cursor.close()
conn.close()
print("Despachantes inseridos com sucesso.")
