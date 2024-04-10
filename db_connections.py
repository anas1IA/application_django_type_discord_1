import pymongo
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb+srv://anasnouri:nHop6rCy56i9DAxM@cluster0.6wmjerh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['test']