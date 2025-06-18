from faker import Faker
import random
from datetime import timedelta
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

def get_ids(tabela):
    cursor.execute(f"SELECT id FROM {tabela}")
    return [row[0] for row in cursor.fetchall()]

clientes_ids = get_ids('clientes')
veiculos_ids = get_ids('veiculos')
despachantes_ids = get_ids('despachantes')

def gerar_locacao():
    data_loc = faker.date_between(start_date='-6M', end_date='today')
    duracao = random.randint(1, 15)
    return (
        random.choice(veiculos_ids),
        random.choice(clientes_ids),
        random.choice(despachantes_ids),
        data_loc,
        data_loc + timedelta(days=duracao),
        round(random.uniform(80, 250) * duracao, 2)
    )

for _ in range(100):
    cursor.execute("""
        INSERT INTO locacoes (veiculo_id, cliente_id, despachante_id, data_locacao, data_entrega, valor_total)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, gerar_locacao())

conn.commit()
cursor.close()
conn.close()
print("Locações inseridas com sucesso.")
