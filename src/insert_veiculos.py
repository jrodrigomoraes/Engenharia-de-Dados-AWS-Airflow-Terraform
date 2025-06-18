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

def gerar_veiculo():
    return (
        faker.date_between(start_date='-3y', end_date='today'),
        random.randint(2010, 2025),
        random.choice(['Onix', 'HB20', 'Corolla', 'Civic', 'Gol', 'Ka', 'Argo', 'Cruze']),
        faker.unique.bothify(text='???-####').upper(),
        random.choice(['Disponível', 'Indisponível', 'Locado']),
        round(random.uniform(80, 250), 2)
    )

for _ in range(30):
    cursor.execute("""
        INSERT INTO veiculos (data_aquisicao, ano, modelo, placa, status, preco_diaria)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, gerar_veiculo())

conn.commit()
cursor.close()
conn.close()
print("Veículos inseridos com sucesso.")
