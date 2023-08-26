from pymongo.mongo_client import MongoClient

# CONEXÃO COM O BANCO DE DADOS DO MONGO
def connectionMongoDB():
  return MongoClient("mongodb+srv://valensoela:Compaq567@projetoimpactaestudo.fq78wqv.mongodb.net/?retryWrites=true&w=majority")

def databaseMongoDB():
  return connectionMongoDB()["api_bitcoin"]