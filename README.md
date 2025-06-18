# 🚗 Projeto de Engenharia de Dados: Locadora de Veículos

Este projeto simula a criação de um pipeline de dados completo para uma empresa fictícia de locação de veículos, utilizando tecnologias modernas de engenharia de dados.

## Objetivos

- Simular um ambiente analítico de uma locadora
- Criar uma base relacional com dados normalizados
- Realizar transformações e disponibilizar dados prontos para BI
- Automatizar o pipeline com Airflow e organizar a infraestrutura com Terraform

## Dados Utilizados

- **Fato:** Locações realizadas
- **Dimensões:** Clientes, veículos, despachantes, tempo
- Dados exportados no formato Parquet e armazenados no Amazon S3
- **Observação:** Os dados foram gerados artificialmente com a biblioteca Faker do Python para simular um cenário realista.

## Arquitetura

Foi utilizado o PostgreSQL tanto de forma local (offline) quanto em uma instância no Amazon RDS. Após a coleta e armazenamento dos dados, foi realizada uma transformação utilizando Apache Spark, com processamento adicional via Amazon Athena para responder perguntas de negócio. Os resultados das transformações foram armazenados no Amazon S3, tanto em seu formato bruto quanto em formatos otimizados para análise com ferramentas de BI.

## Tecnologias

- **PySpark**: Transformação e limpeza dos dados, escrita em formato Parquet.
- **Airflow**: Orquestração dos pipelines de dados.
- **AWS S3**: Armazenamento em camadas (raw, staging e output).
- **Athena**: Consulta de dados diretamente do S3 e exportação de resultados.
- **Terraform**: Para provisionamento da infraestrutura em nuvem.
- **MongoDB**: Para identificar contratos de risco, que estavam no formato json. (É uma etapa opcional)
- **QuickSight**: Ferramenta para visualização dos resultados

## Perguntas que foram respondidas

Após tratar os dados com PySpark, utilizei Athena para responder questões sobre o negócio.

- Quais veículos foram locados em determinados períodos?
- Quais despachantes locaram quais veículos?
- Qual faturamento por período?
- Quais clientes locaram quais veículos?
- Tempo médio de locação por modelo
- Cliente mais fiel (que mais alugou)

## Pipeline de Dados

O pipeline de dados seguiu o seguinte fluxo:
- **Ingestão**: Dados brutos extraídos de um banco PostgreSQL local e do Amazon RDS.
- **Transformação**: Uso de PySpark para limpar, normalizar e criar tabelas fato e dimensões.
-  **Armazenamento**:
   - Camada `raw`: Dados brutos
   - Camada `staging`: Dados organizados por dimensão
   - Camada `output`: Resultados de queries salvos via Athena para BI
- **Orquestração**: Apache Airflow executando DAGs para automação e movimentação dos dados.
- **Identificação de Contratos de Risco**: Uso de MongoDB para visualização de dados em arquivos semi-estruturados
- **Visualização de Dados**: Utilizado ferramentas de BI(aqui pode ser a da sua preferência) para visualizar as bases criadas com Athena.

## Failures

Detalhamento de um erro encontrado durante o projeto. Erros que podem acontecer em um pipeline real.

## Scripts

Os scripts estão organizados nas pastas `src`, `scripts` e `sql`. Seus objetivos incluem:
- Criação do Banco de Dados e Tabelas
- Criação de um `job Spark` para transformação dos dados
- Geração de dados com `Faker` e inserção no banco
- Respostas a perguntas de negócio com queries SQL
- `DAGs do Airflow` para automatização da movimentação entre camadas
- Código para leitura de contratos em JSON via `MongoDB` e identificação de contratos de risco

## Outputs

Dados prontos para ser utilizados em ferramentas de BI, optei por `Amazon QuickSight` por conta da integração com o ambiente AWS.

## Terraform

A infraestrutura básica foi provisionada com Terraform, facilitando a automação e escalabilidade do ambiente analítico com boas práticas de Infrastructure as Code (IaC). Este projeto também está sendo utilizado como parte do meu aprendizado de Terraform.

## Visualização

Resultado das perguntas de negócio em dashboards. Apenas as imagens.
