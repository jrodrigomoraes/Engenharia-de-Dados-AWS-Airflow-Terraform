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

def gerar_cliente():
    return (
        faker.unique.ssn(),
        faker.unique.bothify(text='###########'),
        faker.date_between(start_date='today', end_date='+5y'),
        faker.name(),
        faker.date_between(start_date='-1y', end_date='today'),
        faker.date_of_birth(minimum_age=18, maximum_age=65),
        faker.phone_number(),
        random.choice(['Ativo', 'Inativo'])
    )

for _ in range(50):
    cursor.execute("""
        INSERT INTO clientes (cpf, cnh, validade_cnh, nome, data_cadastro, data_nascimento, telefone, status)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, gerar_cliente())

conn.commit()
cursor.close()
conn.close()
print("Clientes inseridos com sucesso.")
