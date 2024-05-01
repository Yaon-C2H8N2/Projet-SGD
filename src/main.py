from pymongo import MongoClient


def create_films_collection(db):
    db.create_collection('films', validator={
        '$jsonSchema': {
            'bsonType': 'object',
            'required': ['title', 'year', 'directorId', 'actorsId'],
            'properties': {
                'title': {
                    'bsonType': 'string',
                    'description': 'must be a string and is required'
                },
                'year': {
                    'bsonType': 'int',
                    'description': 'must be an integer and is required'
                },
                'directorId': {
                    'bsonType': 'string',
                    'description': 'must be an objectId and is required'
                },
                'actorsId': {
                    'bsonType': 'array',
                    'description': 'must be an array and is required'
                }
            }
        }
    })


def create_cinemas_collection(db):
    db.create_collection('cinemas', validator={
        '$jsonSchema': {
            'bsonType': 'object',
            'required': ['name', 'address', 'movies'],
            'properties': {
                'name': {
                    'bsonType': 'string',
                    'description': 'must be a string and is required'
                },
                'address': {
                    'bsonType': 'string',
                    'description': 'must be a string and is required'
                },
                'movies': {
                    'bsonType': 'array',
                    'description': 'must be an array and is required'
                }
            }
        }
    })


def create_realisateurs_collection(db):
    db.create_collection('realisateurs', validator={
        '$jsonSchema': {
            'bsonType': 'object',
            'required': ['name', 'birthdate', 'nationality'],
            'properties': {
                'name': {
                    'bsonType': 'string',
                    'description': 'must be a string and is required'
                },
                'birthdate': {
                    'bsonType': 'date',
                    'description': 'must be a date and is required'
                },
                'nationality': {
                    'bsonType': 'string',
                    'description': 'must be a string and is required'
                }
            }
        }
    })


def main():
    client = MongoClient('localhost', 27017)
    db = client['projetSGD']

    film = False
    cinema = False
    realisateur = False

    for collection in db.list_collections():
        if collection['name'] == 'films':
            film = True
        if collection['name'] == 'cinemas':
            cinema = True
        if collection['name'] == 'realisateurs':
            realisateur = True

    if not film:
        create_films_collection(db)

    if not cinema:
        create_cinemas_collection(db)

    if not realisateur:
        create_realisateurs_collection(db)


if __name__ == '__main__':
    main()
