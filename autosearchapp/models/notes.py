from django.db import models
from .vehicle import Vehicle

class Note(models.Model):

    vehicle_notes = models.CharField(max_length=200, blank=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = ("note")
        verbose_name_plural = ("notes")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("note_detail", kwargs={"pk": self.pk})
