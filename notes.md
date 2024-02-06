## Conception
L’objectif de cette partie est de choisir une modélisation cohérente des informations en adéquation avec les fonctionnalités retenues.
Cette partie devra contenir un cahier des charges des fonctionnalités qui seront proposées et une explication des informations
modélisées dans la base de données « en clair » et sous forme d’un diagramme UML, et des exemples de document « json » insérés
dans la base. On précisera clairement la ou les collections créées, en les justifiant et en positionnant également ces choix par rapport aux notions
de schéma polymorphique, imbrication ou références vues en CM et TD. La justification des choix de modélisation pourra s'appuyer sur les fonctionnalités attendues décrites dans le cahier des charges de 
l'application, qui pourront être présentées de façon concise dans cette partie et de façon détaillée dans les parties 2 et 3.

## Requêtage
L'objectif de cette partie est de proposer un large panel de requêtes pouvant être nécessaires pour avoir des informations sur les films
et leur diffusion, et des fonctionnalités analytiques jugées pertinentes. Il s'agit de proposer un ensemble diversifié de requêtes avec les différents opérateurs vus en CM/TD et TP, avec des instructions
"find", des instructions "aggregate", et au minimum une requête avec le mécanisme Map-Reduce, en expliquant précisément votre
requête. Des requêtes de mise à jour de la base seront également données. On pourra supposer ici que des données « erronées » ont été
stockées dans la base de données, et que l’on souhaite corriger ou compléter la base (y compris par exemple en ajoutant des
commentaires sur un film).

## Python et PyMongo
L'objectif de cette partie est de proposer des requêtes complémentaires plus complexes que celles décrites dans la partie 2 sur les
jeux mais aussi sur les commentaires et avis des utilisateurs à des fins d'analyse décisionnelle pour les gestionnaires des cinémas.
Il s'agit d'expliquer l'usage du driver pyMongo pour accéder à la base de données MongoDB et de proposer des scripts python plus
avancés pour réaliser des fonctionnalités qui pourraient être utiles soit pour l'utilisateur, soit pour les gestionnaires.