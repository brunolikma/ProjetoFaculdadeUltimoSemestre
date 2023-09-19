# Projeto de Extração de Informações de Partidas

Este projeto tem como objetivo extrair informações de partidas de um endpoint e, em seguida, utilizar essas informações como parâmetros para outro endpoint. O fluxo de trabalho envolve o uso de várias tecnologias, incluindo Python, Databricks, Spark, AWS S3 e Tableau.

## Tecnologias Utilizadas

- **Python**: Utilizaremos Python para escrever os scripts que extrairão os IDs de partidas e farão as chamadas aos endpoints.

- **Databricks**: Databricks será usado para criar um ambiente de análise escalável e gerenciável para processar os dados.

- **Spark**: Utilizaremos o Apache Spark, uma ferramenta de processamento de big data, para manipular os dados extraídos.

- **AWS S3**: Armazenaremos os dados processados no Amazon S3, um serviço de armazenamento em nuvem altamente escalável da AWS.

- **Tableau**: Utilizaremos o Tableau para criar visualizações e painéis de controle com as informações extraídas.

## Fluxo de Trabalho

1. **Extração de IDs de Partidas**:
   - Utilize o Python para fazer uma chamada ao endpoint que contém as informações das partidas.
   - Extraia os IDs das partidas a partir da resposta.

2. **Transformação de Dados com Spark**:
   - Carregue os IDs das partidas em um ambiente Databricks.
   - Utilize o Apache Spark para transformar e processar os dados conforme necessário.

3. **Armazenamento no AWS S3**:
   - Após o processamento, armazene os dados transformados no Amazon S3.

4. **Extração de Informações de Partidas**:
   - Utilize o Python para fazer chamadas aos endpoints de informações das partidas, passando os IDs como parâmetros.
   - Extraia as informações das partidas a partir das respostas.

5. **Visualização com Tableau**:
   - Importe os dados extraídos do S3 para o Tableau.
   - Crie visualizações e painéis de controle para analisar e apresentar as informações das partidas.

## Configuração e Execução

1. **Configuração do Ambiente Databricks**:
   - Configure um ambiente Databricks com as bibliotecas necessárias para Python e Spark.

2. **Código Python**:
   - Desenvolva os scripts em Python para a extração de IDs de partidas e a extração de informações das partidas.

3. **Integração com AWS S3**:
   - Configure as credenciais e permissões necessárias para acessar o Amazon S3.

4. **Integração com Tableau**:
   - Configure a integração do Tableau com o Amazon S3 para importar dados.

5. **Agendamento de Tarefas**:
   - Agende tarefas para executar o fluxo de trabalho em intervalos regulares, se necessário.

## Executando o Projeto

1. Execute os scripts Python no ambiente Databricks para extrair e processar os dados.

2. Armazene os dados transformados no Amazon S3.

3. Configure o Tableau para importar os dados do S3 e criar visualizações.

4. Monitore e ajuste o fluxo de trabalho conforme necessário.

## Licença

Este projeto é distribuído sob a [licença MIT](LICENSE), que permite o uso, modificação e distribuição, desde que seja incluída a atribuição apropriada.
