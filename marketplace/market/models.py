from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        chaine = f"{self.name} - {self.price} - {self.quantity}"
        return chaine

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    grade = models.CharField(max_length=100, default="Acheteur")

    def __str__(self):
        chaine = f"{self.name} - {self.email}"
        return chaine

    def verify(self, username, password):
        if self.name == username and self.password == password:
            return True
        else:
            return False

    def get_grade(self):
        return self.grade