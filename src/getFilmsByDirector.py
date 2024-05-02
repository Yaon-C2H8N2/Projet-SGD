from dbutils import Connection

connection = Connection()
db = connection.db

def get_films_by_director_name(director_name):
    # Trouver l'ID du réalisateur basé sur son nom
    director = db.realisateurs.find_one({"name": director_name})
    if director is None:
        return []  # Aucun réalisateur trouvé avec ce nom

    # Utiliser l'ID du réalisateur pour trouver ses films
    films = db.films.find({"director": director["_id"]})
    return list(films)

if __name__ == '__main__':
    films = get_films_by_director_name("Christopher Nolan")
    for film in films:
        print(film["title"] + " (" + str(film["year"]) + ")" + " : " + str(film["actors"]))
