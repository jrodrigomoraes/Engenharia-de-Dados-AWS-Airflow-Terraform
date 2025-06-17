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
