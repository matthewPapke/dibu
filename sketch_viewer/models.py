from django.db import models

class Artist(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    num_sketches = models.IntegerField()


class Sketch(models.Model):
    name = models.CharField(max_length=100)
    models.ForeignKey(Artist, on_delete=models.CASCADE)