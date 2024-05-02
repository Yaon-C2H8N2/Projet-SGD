from dbutils import Connection

connection = Connection()
db = connection.db


def realisateursbymaxoccupency():
    results = db.cinemas.aggregate([
        {"$unwind": "$projections"},
        {"$project": {"_id": 0, "projection": "$projections"}},
        {"$lookup": {"from": "films", "localField": "projection.filmid", "foreignField": "_id", "as": "film"}},
        {"$project": {"_id": 0, "director": "$film.director", "occupancy": "$projection.occupancy"}},
        {"$lookup": {"from": "realisateurs", "localField": "director", "foreignField": "_id", "as": "director"}},
        {"$project": {"_id": 0, "name": "$director.name", "occupancy": 1}},
        {"$group": {"_id": "$name", "occupation": {"$avg": {"$divide": ["$occupancy.reserved", "$occupancy.total"]}}}},
        {"$project": {"_id": 0, "name": "$_id", "occupation": {"$multiply": ["$occupation", 100]}}},
        {"$sort": {"occupation": -1}}
    ])

    for result in results:
        print(result)

if __name__ == '__main__':
    print("Realisateurs par taux d'occupation maximal :")
    realisateursbymaxoccupency()
