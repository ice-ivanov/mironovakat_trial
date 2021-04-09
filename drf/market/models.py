from django.db import models
from custom_auth.models import User


class Animal(models.Model):
    ANIMAL_TYPE_CHOICE = (
        ('cat', 'Cat'),
        ('hedgehog', 'Hedgehog'),
    )
    name = models.CharField(max_length=255, unique=True)
    type = models.CharField(max_length=20, choices=ANIMAL_TYPE_CHOICE)
    breed = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Lot(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    price = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    winner_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.owner}'s {self.animal.name}"


class Bid(models.Model):
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE)
    value = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.owner} for {self.lot}'
