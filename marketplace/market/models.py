from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=False)
    quantity = models.IntegerField(blank=False)
    vendeur_id = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        chaine = f"Nom : {self.name}\rPrix : {self.price}\rDescription : {self.description}\rQuantité : {self.quantity}\rVendeur : {self.vendeur_id}"
        return chaine

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        chaine = f"{self.name} - {self.email}"
        return chaine

    def verify(self, username, password):
        if self.name == username and check_password(password, self.password):
            return True
        else:
            return False

class Commande(models.Model):
    item_id = models.ForeignKey('Item', on_delete=models.CASCADE)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    vendeur_id = models.ForeignKey('User', on_delete=models.CASCADE, related_name='vendeur')
    quantity = models.IntegerField(blank=False)
    prix = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        chaine = f"Item : {self.item_id}\rUser : {self.user_id}\rQuantité : {self.quantity}"
        return chaine