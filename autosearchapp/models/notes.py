from django.db import models
from .vehicle import Vehicle

class Note(models.Model):

    vehicle_notes = models.CharField(max_length=200)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("note")
        verbose_name_plural = ("notes")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("note_detail", kwargs={"pk": self.pk})
