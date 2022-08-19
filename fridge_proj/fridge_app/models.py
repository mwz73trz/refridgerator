from .enums import Measurement
from distutils.command.upload import upload
from django.db import models
from django.core.validators import MinValueValidator


class Food(models.Model):
    title = models.CharField(max_length=25)
    pic = models.ImageField(upload_to='images/')
    amount = models.IntegerField(validators=[MinValueValidator(0)])
    best_before_end = models.DateField()
    amount_type = models.CharField(max_length=6, choices=Measurement.choices, default=Measurement.NOTHING)

    def __str__(self):
        return self.title
