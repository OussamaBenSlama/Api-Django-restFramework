from django.db import models

# Create your models here.


class Note(models.Model):
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.body[0:50]

class Personne(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='image/')
    def __str__(self):
        return self.name