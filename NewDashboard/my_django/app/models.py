from django.db import models


class App(models.Model):
    title = models.CharField(max_length=100)
    image  = models.ImageField(storage='images/',default = 'value')