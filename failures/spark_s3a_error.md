## Falhas

Durante o desenvolvimento deste projeto, enfrentei algumas dificuldades, sendo uma delas a conexão entre o PySpark e o S3. O principal erro ocorreu ao tentar salvar os dados diretamente no S3, o que resultou em dificuldades na identificação da causa exata.

### Erro encontrado:

`
Py4JJavaError: An error occurred while calling ...
java.lang.ClassNotFoundException: Class org.apache.hadoop.fs.s3a.S3AFileSystem not found

`


## Tentativa de Solução

Após realizar diversas pesquisas e analisar o log de erro, identifiquei que o problema estava relacionado ao conector Hadoop-AWS. Para tentar resolver, fiz algumas ações, como:

- Instalar os pacotes necessários.
- Configurar corretamente as permissões AWS.
  
Apesar dessas tentativas, o problema persistiu.

## Alternativa

Como solução alternativa, optei por salvar os arquivos no S3 de forma compactada (em formato ZIP). Embora isso tenha resolvido o problema imediato, gerou tarefas adicionais no processo, pois tive que implementar um job no AWS Glue para descompactar e organizar os arquivos.

## Próximos Passos

Ainda estou investigando o erro para encontrar uma solução definitiva, com o objetivo de evitar o uso de compactação como uma medida paliativa no futuro.
