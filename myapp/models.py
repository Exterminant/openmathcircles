from django.db import models
from datetime import datetime

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    organization = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=300)
    brief_info = models.TextField()
    description = models.TextField(default="sample description")
    zoom_link = models.TextField(default="await")
    date_of_event = models.DateTimeField(default=datetime.now)
    recommended_literature = models.TextField(default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
