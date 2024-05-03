# Systèmes de Gestion de Documents - Projet

## Introduction

Ce projet se concentre sur l'utilisation de la base de données NoSQL MongoDB pour modéliser, insérer et manipuler des
données. L'objectif est d'acquérir une expertise dans cette technologie, qui offre une flexibilité et une capacité à
gérer de grands ensembles de données.

## Exécution

### Création des collections

Les collections peuvent être créés en exécutant les commandes mongosh contenues dans le
fichier `collection_creation.txt`.

### Insertion des données

Les données peuvent être insérées en exécutant les commandes mongosh contenues dans le fichier `collection_insert.txt`.

### Requêtes

Différentes requêtes fournies dans `mongo_request.txt` peuvent être exécutées.

### Python

Des scripts Python sont fournis pour effectuer des opérations sur la base de données. Pour permettre aux scripts de se
connecter à MongoDB, il est nécessaire de modifier les variables suivantes par les informations de connexion adéquates dans le script `src/dbutils.py` :

```python
username = 'root'
password = 'root'
auth_source = 'admin'
host = 'localhost'
database = 'projetSGD'
port = 27017
```

Ils peuvent être exécutés depuis le dossier `src` en utilisant la commande `python3 nom_du_script.py`.