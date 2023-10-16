# Databricks notebook source
!pip install pyspark
!pip install findspark

# COMMAND ----------

import findspark
findspark.init()

# COMMAND ----------

from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
import requests
from pyspark.sql import functions as F
from pyspark.sql.types import *
import json

# COMMAND ----------

# Creating a spark session
spark = SparkSession \
    .builder \
    .appName("ProjetoFaculdade") \
    .config("spark.master", "local") \
    .getOrCreate()

# COMMAND ----------

# MAGIC %run ../ProjetoFaculdade/Credenciais

# COMMAND ----------

partida = requests.get(f'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=100&api_key={api_key}').json()

# COMMAND ----------

list = ['']

# COMMAND ----------

df_auxiliar = []

# COMMAND ----------

df = spark.createDataFrame([list],["Partida"])

# COMMAND ----------

for x in partida:
    df_auxiliar = spark.createDataFrame([x], StringType())
    df = df.union(df_auxiliar)

# COMMAND ----------

df.show()

# COMMAND ----------

df = df.where(df.Partida != '')

# COMMAND ----------

df.show()

# COMMAND ----------

df.repartition(1).write.csv(path+'Projeto-Faculdade')

# COMMAND ----------

aws_s3_df.show()

# COMMAND ----------

aws_s3_df = spark.read.csv(path+'Projeto-Faculdade')
aws_s3_df.show()

# COMMAND ----------

### Inicio AC2

# COMMAND ----------

aws_s3_df = aws_s3_df.withColumnRenamed("_c0", "ID_Partida")

# COMMAND ----------

aws_s3_df.show()

# COMMAND ----------

id_partida = (aws_s3_df.select('ID_Partida').
      rdd.flatMap(lambda x: x).collect())

# COMMAND ----------

for x in range(len(id_partida)):
    historico_dados_partida = requests.get(f'{endpoint_partida}{id_partida[x]}?api_key={api_key}').json()
    jsonData = json.dumps(historico_dados_partida)

    jsonDataList = []
    jsonDataList.append(jsonData)

    jsonRDD = sc.parallelize(jsonDataList)
    df = spark.read.json(jsonRDD)
    df.repartition(1).write.json(path+f'{id_partida[x]}')

# COMMAND ----------


