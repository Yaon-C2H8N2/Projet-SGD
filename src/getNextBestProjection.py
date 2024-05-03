from dbutils import Connection

connection = Connection()
db = connection.db


def get_available_places_by_cinema(title):
    # Récupérer toutes les projections d'un film donné
    places_by_cinema = db.cinemas.aggregate([
        {"$unwind": "$projections"},
        {"$project": {"_id": 0, "name": "$name", "projection": "$projections"}},
        {"$match": {"projection.filmid": db.films.find_one({"title": title})["_id"]}},
        {"$project": {"_id": 0, "name": 1, "datetime": "$projection.datetime", "availablePlaces": {"$subtract": ["$projection.occupancy.total", "$projection.occupancy.reserved"]}}},
    ])

    return places_by_cinema


def map(values):
    result = {} # Accumulateur du map
    for value in values:
        if value["name"] not in result:
            result[value["name"]] = [] # Si une clé n'est pas dans l'accumulateur, on l'ajoute
        # Ajout du tuple (places disponibles, date) pour la clé cinema
        result[value["name"]].append((value["availablePlaces"], value["datetime"]))
    return result

def reduce(values):
    result = {} # Accumulateur du reduce
    for cinema, projections in values.items():
        # On réduit chaque valeur pour une clé en prenant la projection avec le plus de places disponibles
        best_projection = max(projections, key=lambda x: x[0])
        result[cinema] = best_projection
    return result



if __name__ == '__main__':
    # Map
    all_avail = get_available_places_by_cinema("The Social Network")
    mapped_values = map(all_avail)
    # Reduce
    reduced_values = reduce(mapped_values)
    # Une simple fonction d'aggregation aurait pu être utilisée pour obtenir le même résultat
    # Ici, on a utilisé un map/reduce pour correspondre à l'exercice
    # Mais au final les fonctions d'aggregation sont ni plus ni moins que des map/reduce simplifiés
    # NB: La fonction mapReduce de mongodb est dépréciée depuis la version 4.4 en faveur des pipelines d'aggregation
    for cinema, projection in reduced_values.items():
        print(cinema + " : " + str(projection[1]) + " (" + str(projection[0]) + " places disponibles)")
