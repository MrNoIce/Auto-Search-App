from django.db import models
from django.contrib.auth.models import User

class Vehicle(models.Model):

    heading = models.CharField(max_length=50, null=True, blank=True)
    mileage = models.IntegerField(max_length=6, null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)
    vin = models.CharField(max_length=50, null=True, blank=True)
    zip_code = models.IntegerField(max_length=7, null=True, blank=True)
    vdp_url = models.URLField(max_length=200, null=True, blank=True)
    price = models.IntegerField(max_length=50, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = ("vehicle")
        verbose_name_plural = ("vehicles")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("vehicle_detail", kwargs={"pk": self.pk})
