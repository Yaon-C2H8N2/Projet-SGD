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

    print("Insertion d'un film dans la collection films")
    print(db['films'].insert_one({
        'title': 'The Dark Knight',
        'year': 2008,
        'directorId': '5f3d3a5b0f3d5c4e4d3d5f3d',
        'actorsId': ['5f3d3a5b0f3d5c4e4d3d5f3d', '5f3d3a5b0f3d5c4e4d3d5f3d']
    }).inserted_id)


if __name__ == '__main__':
    main()
