from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} {self.model} ({self.year})"
class Owner(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    car = models.OneToOneField(Car, on_delete=models.CASCADE)

    def __str__(self):
        return self.name