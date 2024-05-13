# Endpoint

Liste des items : `/market/items`
Ajout d'un item : `/market/items/add`
Suppression d'un item : `/market/items/delete/id`
Modification d'un item : `/market/items/update/id`

Liste des utilisateurs : `/market/users`
Ajout d'un utilisateur : `/market/users/add`
Suppression d'un utilisateur : `/market/users/delete/id`
Modification d'un utilisateur : `/market/users/update/id`

# Grades possibles

- Fondateur (Il est le seul possible à pouvoir donner le grade "Administrateur" et possède toutes les permissions comme les Administrateurs)
- Administrateur (Les administrateurs peuvent donner le grade "Vendeur" et ont toutes les permissions de modération concernant le site)
- Vendeur (Un vendeur peut ajouter des items à vendre et modifier ces derniers)
- Acheteur (Ne possède aucune permission à part la possibilité d'acheter des items)