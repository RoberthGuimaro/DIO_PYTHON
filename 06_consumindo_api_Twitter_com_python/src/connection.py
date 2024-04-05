from src.services import USER_NAME_MONGO, PASSWORD_MONGO
import pymongo as pyM

# Cria o cliente Mongo na variavel
client = pyM.MongoClient(f"mongodb+srv://{USER_NAME_MONGO}:{PASSWORD_MONGO}<@cluster0.ztguhzg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Seta a base na variavel
db = client.dio_tweepy

# cria a colecao no db
trends_collection = db.trends