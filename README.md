# R209 - Projet CRUD Marketplace

## Description

Le projet consiste à créer une boutique en ligne avec les fonctionnalités CRUD (Create, Read, Update, Delete) pour les items et les utilisateurs. Le site peut être utilisé pour autre chose qu'une boutique puisqu'il n'y a pas de section "panier / mes commandes" et "paiement".

## Fonctionnalités

Listez ici les principales fonctionnalités de votre projet. Par exemple :

- Fonctionnalité 1 : Description de la fonctionnalité 1.
- Fonctionnalité 2 : Description de la fonctionnalité 2.
- Fonctionnalité 3 : Description de la fonctionnalité 3.

## Installation & lancement du projet

Il suffit de cloner le projet, d'y installer les dépendances puis de lancer le serveur.
```bash
git clone https://github.com/Xurron/r209-crud-project.git
cd r209-crud-project
python -m venv venv
python -m pip install -r requirements.txt
cd marketplace
python manage.py runserver
```

## à faire
- détail pages HTML
- mise en place d'un retrait d'un article quand on commande et quand un utilisateur supprime son compte (ça supprime tous les articles au quel il est vendeur)
- CSS
- faire de vrai utilisateur et les mettres dans le readme
- se connecter directement quand on créer un compte

### Endpoint

Liste des items : `/market/items`
Ajout d'un item : `/market/items/add`
Suppression d'un item : `/market/items/delete/id`
Modification d'un item : `/market/items/update/id`

Liste des utilisateurs : `/market/users`
Ajout d'un utilisateur : `/market/users/add`
Suppression d'un utilisateur : `/market/users/delete/id`
Modification d'un utilisateur : `/market/users/update/id`