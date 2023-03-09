from django.db import models

# Create your models here.


class DataBase(models.Model):
    file = models.FileField()
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
