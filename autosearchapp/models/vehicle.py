from django.db import models
from django.contrib.auth.models import User

class Vehicle(models.Model):

    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField(max_length=4)
    mileage = models.IntegerField(max_length=6)
    color = models.CharField(max_length=50)
    vin = models.CharField(max_length=50)
    zip_code = models.IntegerField(max_length=7)
    url = models.URLField(max_length=200)
    price = models.IntegerField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("vehicle")
        verbose_name_plural = ("vehicles")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("vehicle_detail", kwargs={"pk": self.pk})
