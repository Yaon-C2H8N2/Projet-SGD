from pymongo import MongoClient

username = 'root'
password = 'root'
auth_source = 'admin'
host = 'localhost'
database = 'projetSGD'
port = 27017


class Connection:
    def __init__(self):
        client = MongoClient(host=host,
                             port=port,
                             username=username,
                             password=password,
                             authSource=auth_source)
        self.db = client[database]
