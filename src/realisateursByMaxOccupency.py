from dbutils import Connection

connection = Connection()
db = connection.db


def realisateursbymaxoccupency():
    results = db.cinemas.aggregate([
        # On déplie toutes les projections
        {"$unwind": "$projections"},
        # On projette uniquement la projection
        {"$project": {"_id": 0, "projection": "$projections"}},
        # On lie les ObjectId des films aux projections pour pouvoir récupérer le réalisateur
        {"$lookup": {"from": "films", "localField": "projection.filmid", "foreignField": "_id", "as": "film"}},
        # On projette uniquement le réalisateur et les informations d'occupation des salles
        {"$project": {"_id": 0, "director": "$film.director", "occupancy": "$projection.occupancy"}},
        # On lie les ObjectId des réalisateurs aux projections
        {"$lookup": {"from": "realisateurs", "localField": "director", "foreignField": "_id", "as": "director"}},
        # On projette uniquement le nom du réalisateur et les informations d'occupation des salles
        {"$project": {"_id": 0, "name": "$director.name", "occupancy": 1}},
        # On groupe par réalisateur et on calcule le taux d'occupation moyen
        {"$group": {"_id": "$name", "occupation": {"$avg": {"$divide": ["$occupancy.reserved", "$occupancy.total"]}}}},
        # On projette le nom du réalisateur et le taux d'occupation en pourcentage
        {"$project": {"_id": 0, "name": "$_id", "occupation": {"$multiply": ["$occupation", 100]}}},
        # On trie par taux d'occupation décroissant
        {"$sort": {"occupation": -1}}
    ])

    for result in results:
        print(result)

if __name__ == '__main__':
    print("Realisateurs par taux d'occupation maximal :")
    realisateursbymaxoccupency()
