from django.db import models


# Create your models here.
class Visit(models.Model):
    number_of_visits = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Visit"
        verbose_name_plural = "Visits"
