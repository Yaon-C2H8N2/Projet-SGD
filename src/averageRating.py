from dbutils import Connection

connection = Connection()
db = connection.db

def calculate_average_ratings():
    # On déplie les reviews de tous les films pour pouvoir les agréger
    pipeline = [
        {"$unwind": "$reviews"},
        {"$group": {
            "_id": "$_id",
            # On calcule la moyenne des notes des reviews lors du regroupement
            "average_rating": {"$avg": "$reviews.rating"}
        }}
    ]
    return list(db.films.aggregate(pipeline))

if __name__ == '__main__':
    print("Note moyenne des films :")
    avg_ratings = calculate_average_ratings()
    for avg_rating in avg_ratings:
        print(db.films.find_one({"_id": avg_rating["_id"]})["title"] + " : " + str(avg_rating["average_rating"]) + "/5")