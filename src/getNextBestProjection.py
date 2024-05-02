from dbutils import Connection

connection = Connection()
db = connection.db


def get_available_places_by_cinema(title):
    places_by_cinema = db.cinemas.aggregate([
        {"$unwind": "$projections"},
        {"$project": {"_id": 0, "name": "$name", "projection": "$projections"}},
        {"$match": {"projection.filmid": db.films.find_one({"title": title})["_id"]}},
        {"$project": {"_id": 0, "name": 1, "datetime": "$projection.datetime", "availablePlaces": {"$subtract": ["$projection.occupancy.total", "$projection.occupancy.reserved"]}}},
    ])

    return places_by_cinema


def map(values):
    result = {}
    for value in values:
        if value["name"] not in result:
            result[value["name"]] = []
        result[value["name"]].append((value["availablePlaces"], value["datetime"]))
    return result

def reduce(values):
    result = {}
    for cinema, projections in values.items():
        best_projection = max(projections, key=lambda x: x[0])
        result[cinema] = best_projection
    return result



if __name__ == '__main__':
    all_avail = get_available_places_by_cinema("The Social Network")
    mapped_values = map(all_avail)
    reduced_values = reduce(mapped_values)
    for cinema, projection in reduced_values.items():
        print(cinema + " : " + str(projection[1]) + " (" + str(projection[0]) + " places disponibles)")
