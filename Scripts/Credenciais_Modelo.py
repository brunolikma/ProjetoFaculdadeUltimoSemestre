# Databricks notebook source
# MAGIC %md
# MAGIC ## Config API Riot Games

# COMMAND ----------

import requests

# COMMAND ----------

streamer_nickname = ''

# COMMAND ----------

api_key = ''
link_summoner = f'https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{streamer_nickname}?api_key={api_key}'

# COMMAND ----------

request_summoner = requests.get(link_summoner).json()

# COMMAND ----------

id = request_summoner['id']
accountId = request_summoner['accountId']
puuid = request_summoner['puuid']
name = request_summoner['name']
profileIconId = request_summoner['profileIconId']
revisionDate = request_summoner['revisionDate']
summonerLevel = request_summoner['summonerLevel']

# COMMAND ----------

# MAGIC %md
# MAGIC ## Config AWS

# COMMAND ----------

access_key = ''
secret_key = ''
aws_s3_bucket = ''
mount_name = '/mnt/mount_s3'

source_url = "s3a://%s:%s@%s" %(access_key,secret_key,aws_s3_bucket)

# COMMAND ----------

dbutils.fs.mount(source_url,mount_name)

# COMMAND ----------

# MAGIC %fs ls '/mnt/mount_s3'

# COMMAND ----------

path = ''