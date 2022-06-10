from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    avtor = models.CharField(max_length=100)
    type_book = models.CharField(max_length=50)
    about_book = models.TextField()
    

    def __str__(self):
        return self.title