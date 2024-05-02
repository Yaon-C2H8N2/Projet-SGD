from bson import Code
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime


username = 'root'
password = 'root'
auth_source = 'admin'  # The database to authenticate against, usually 'admin'
host = 'localhost'
port = 27017

# Create a MongoDB client with authentication
client = MongoClient(host=host,
                     port=port,
                     username=username,
                     password=password,
                     authSource=auth_source)
db = client['projetSGD']
collection = db['movies']

# Suppression des collections existantes pour repartir de zéro
db.drop_collection('films')
db.drop_collection('realisateurs')
db.drop_collection('cinemas')


def parse_date(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d")


# Création des collections avec des schémas validés
def create_collections():
    db.create_collection('films', validator={
        '$jsonSchema': {
            'bsonType': 'object',
            'required': ['title', 'year', 'director', 'actors'],
            'properties': {
                'title': {'bsonType': 'string', 'description': 'must be a string and is required'},
                'year': {'bsonType': 'int', 'description': 'must be an integer and is required'},
                'director': {'bsonType': 'objectId', 'description': 'must be an objectId and is required'},
                'actors': {'bsonType': 'array', 'items': {'bsonType': 'string'}, 'description': 'must be an array of strings and is required'}
            }
        }
    })

    db.create_collection('realisateurs', validator={
        '$jsonSchema': {
            'bsonType': 'object',
            'required': ['name', 'birthdate', 'nationality'],
            'properties': {
                'name': {'bsonType': 'string', 'description': 'must be a string and is required'},
                'birthdate': {'bsonType': 'date', 'description': 'must be a date and is required'},
                'nationality': {'bsonType': 'string', 'description': 'must be a string and is required'}
            }
        }
    })

    db.create_collection('cinemas', validator={
        '$jsonSchema': {
            'bsonType': 'object',
            'required': ['name', 'address', 'movies'],
            'properties': {
                'name': {'bsonType': 'string', 'description': 'must be a string and is required'},
                'address': {'bsonType': 'string', 'description': 'must be a string and is required'},
                'movies': {'bsonType': 'array', 'items': {'bsonType': 'objectId'}, 'description': 'must be an array of objectIds and is required'}
            }
        }
    })

# Initialisation des collections
create_collections()

# Insertion des réalisateurs
realisateur_ids = {
    "Christopher Nolan": ObjectId(),
    "Quentin Tarantino": ObjectId(),
    "Francis Ford Coppola": ObjectId(),
    "Frank Darabont": ObjectId(),
    "David Fincher": ObjectId(),
    "Robert Zemeckis": ObjectId(),
    "Lana Wachowski": ObjectId(),
    "James Cameron": ObjectId(),
    "Ridley Scott": ObjectId()
}

realisateurs = [
    {"_id": realisateur_ids["Christopher Nolan"], "name": "Christopher Nolan", "birthdate": parse_date("1970-07-30"), "nationality": "British"},
    {"_id": realisateur_ids["Quentin Tarantino"], "name": "Quentin Tarantino", "birthdate": parse_date("1963-03-27"), "nationality": "American"},
    {"_id": realisateur_ids["Francis Ford Coppola"], "name": "Francis Ford Coppola", "birthdate": parse_date("1939-04-07"), "nationality": "American"},
    {"_id": realisateur_ids["Frank Darabont"], "name": "Frank Darabont", "birthdate": parse_date("1959-01-28"), "nationality": "French-Hungarian"},
    {"_id": realisateur_ids["David Fincher"], "name": "David Fincher", "birthdate": parse_date("1962-08-28"), "nationality": "American"},
    {"_id": realisateur_ids["Robert Zemeckis"], "name": "Robert Zemeckis", "birthdate": parse_date("1951-05-14"), "nationality": "American"},
    {"_id": realisateur_ids["Lana Wachowski"], "name": "Lana Wachowski", "birthdate": parse_date("1965-06-21"), "nationality": "American"},
    {"_id": realisateur_ids["James Cameron"], "name": "James Cameron", "birthdate": parse_date("1954-08-16"), "nationality": "Canadian"},
    {"_id": realisateur_ids["Ridley Scott"], "name": "Ridley Scott", "birthdate": parse_date("1937-11-30"), "nationality": "British"}

]

db.realisateurs.insert_many(realisateurs)

# Insertion des films avec référence aux réalisateurs
films = [
    {"title": "Inception", "year": 2010, "director": realisateur_ids["Christopher Nolan"], "actors": ["Leonardo DiCaprio", "Joseph Gordon-Levitt"]},
    {"title": "Pulp Fiction", "year": 1994, "director": realisateur_ids["Quentin Tarantino"], "actors": ["John Travolta", "Uma Thurman"]},
    {"title": "The Godfather", "year": 1972, "director": realisateur_ids["Francis Ford Coppola"], "actors": ["Marlon Brando", "Al Pacino"]},
    {"title": "The Shawshank Redemption", "year": 1994, "director": realisateur_ids["Frank Darabont"], "actors": ["Tim Robbins", "Morgan Freeman"]},
    {"title": "Fight Club", "year": 1999, "director": realisateur_ids["David Fincher"], "actors": ["Brad Pitt", "Edward Norton"]},
    {"title": "Forrest Gump", "year": 1994, "director": realisateur_ids["Robert Zemeckis"], "actors": ["Tom Hanks", "Robin Wright"]},
    {"title": "The Matrix", "year": 1999, "director": realisateur_ids["Lana Wachowski"], "actors": ["Keanu Reeves", "Laurence Fishburne"]},
    {"title": "Avatar", "year": 2009, "director": realisateur_ids["James Cameron"], "actors": ["Sam Worthington", "Zoe Saldana"]},
    {"title": "Gladiator", "year": 2000, "director": realisateur_ids["Ridley Scott"], "actors": ["Russell Crowe", "Joaquin Phoenix"]}

]

film_ids = db.films.insert_many(films).inserted_ids

# Insertion des cinémas avec les films qu'ils diffusent
cinemas = [
    {"name": "Grand Screen Cinema", "address": "789 Filmstrip Blvd, Bigtown", "movies": [film_ids[0], film_ids[1]]},
    {"name": "Indie Film House", "address": "456 Art St, Smalltown", "movies": [film_ids[2], film_ids[3]]},
    {"name": "Cinema Lux", "address": "321 Lux Rd, Luxuryville", "movies": [film_ids[4], film_ids[5]]},
    {"name": "Retro Cinema", "address": "123 Vintage Ave, Oldtown", "movies": [film_ids[6]]}

]

db.cinemas.insert_many(cinemas)

def calculate_average_ratings():
    pipeline = [
        {"$unwind": "$reviews"},
        {"$group": {
            "_id": "$_id",
            "average_rating": {"$avg": "$reviews.rating"}
        }}
    ]
    return list(db.films.aggregate(pipeline))
def get_films_by_director_name(director_name):
    # Trouver l'ID du réalisateur basé sur son nom
    director = db.realisateurs.find_one({"name": director_name})
    if director is None:
        return []  # Aucun réalisateur trouvé avec ce nom

    # Utiliser l'ID du réalisateur pour trouver ses films
    films = db.films.find({"director": director["_id"]})
    return list(films)

def add_review_to_film(film_title, review):
    result = db.films.update_one(
        {"title": film_title},
        {"$push": {"reviews": review}}
    )
    return result.modified_count


print(get_films_by_director_name("Christopher Nolan"))

review = {"username": "new_critic", "comment": "An interesting take.", "rating": 4}
print(add_review_to_film("Inception", review))

print(calculate_average_ratings())

