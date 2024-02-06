from pymongo import MongoClient

def main():
    client = MongoClient('localhost', 27017)
    db = client['projetSGD']

    for collection in db.list_collections():
        print(collection)

if __name__ == '__main__':
    main()
