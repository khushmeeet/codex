from djongo import models


class Notes(models.Model):
    name = models.TextField(max_length=100)
