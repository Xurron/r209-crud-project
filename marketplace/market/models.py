from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        chaine = f"{self.name} - {self.price} - {self.quantity}"
        return chaine