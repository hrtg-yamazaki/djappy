from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=4095)

    def __str__(self):
        return self.title