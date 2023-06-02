from django.db import models

# Create your models here.
class Book(models.Model):
    Title=models.CharField(max_length=100)
    Author=models.CharField(max_length=100)
    ISBN=models.IntegerField()
    Publisher=models.CharField(max_length=100)

    def __str__(self):
        return self.Title

