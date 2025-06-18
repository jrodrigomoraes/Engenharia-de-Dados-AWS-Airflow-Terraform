CREATE TABLE IF NOT EXISTS clientes(
  id SERIAL PRIMARY KEY,
  cpf VARCHAR(14) UNIQUE NOT NULL,
  cnh VARCHAR(20) UNIQUE NOT NULL,
  validade_cnh DATE NOT NULL,
  nome VARCHAR(100) NOT NULL,
  data_cadastro DATE NOT NULL,
  data_nascimento DATE NOT NULL,
  telefone VARCHAR(20),
  status VARCHAR(10) CHECK (status IN ('Ativo', 'Inativo'))
);

CREATE TABLE IF NOT EXISTS veiculos (
  id SERIAL PRIMARY KEY,
  data_aquisicao DATE NOT NULL,
  ano INTEGER NOT NULL,
  modelo VARCHAR(100) NOT NULL,
  placa VARCHAR(10) NOT NULL,
  status VARCHAR(20) CHECK (status IN ('Disponível', 'Indisponível', 'Locado')),
  preco_diaria NUMERIC(10, 2) NOT NULL
);

CREATE TABLE IF NOT EXISTS despachantes (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  status VARCHAR(10) CHECK (status IN ('Ativo', 'Inativo')),
  filial VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS locacoes (
  id SERIAL PRIMARY KEY,
  veiculo_id INTEGER REFERENCES veiculos(id),
  cliente_id INTEGER REFERENCES clientes(id),
  despachante_id INTEGER REFERENCES despachantes(id),
  data_locacao DATE NOT NULL,
  data_entrega DATE,
  valor_total NUMERIC(10, 2) NOT NULL
);