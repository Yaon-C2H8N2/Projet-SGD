from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.projetSGD
films = db.films

films.insert_one(
    {
        "title": "The Godfather",
        "director": "Francis Ford Coppola",
        "year": 1972
    }
)