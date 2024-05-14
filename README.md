# R209 - Projet CRUD Marketplace

## Description & présentation du projet

Le projet consiste à créer une boutique en ligne avec les fonctionnalités CRUD (Create, Read, Update, Delete) pour les items et les utilisateurs. Le site peut être utilisé pour autre chose qu'une boutique puisqu'il n'y a pas de section "panier / mes commandes" et "paiement".

Le projet inclut les fonctionnalités suivantes :
- CRUD pour les items
- CRUD pour les utilisateurs
- Authentification des utilisateurs
- Système de réception des commandes

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

<u>Lien pour accéder au serveur :</u> http://127.0.0.1:8000/market/login/

<u>Les comptes utilisateurs déjà créés :</u>
- Nom d'utilisateur : `admin` & Mot de passe : `admin`
- Nom d'utilisateur : `toto` & Mot de passe : `toto`

### Liste des endpoint

- Accueil : `/market/` ⚠️ Si vous n'êtes pas connecté, vous serez redirigé vers la page de connexion
- Connexion : `/market/login/`
- Déconnexion : `/market/logout/`


- Détail d'un item : `/market/items/id`
- Ajout d'un item : `/market/items/add`
- Suppression d'un item : `/market/items/delete/id` ⚠️ Il faut être propriétaire de l'item pour le supprimer
- Modification d'un item : `/market/items/update/id` ⚠️ Il faut être propriétaire de l'item pour le modifier


- Détail d'un utilisateur : `/market/users/id`
- Ajout d'un utilisateur : `/market/users/add`
- Suppression d'un utilisateur : `/market/users/delete/id` ⚠️ Il est impossible de supprimer un autre utilisateur que soi-même
- Modification d'un utilisateur : `/market/users/update/id` ⚠️ Il est impossible de modifier un autre utilisateur que soi-même


- Liste des commandes : `/market/commandes/` ⚠️ Il est impossible d'accéder aux commandes des autres utilisateurs
- Suppression d'une commande : `/market/commandes/delete/id` ⚠️ Il est impossible de supprimer une commande qui ne vous appartient pas