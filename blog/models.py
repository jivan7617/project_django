from django.db import models

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=250)
    content=models.TextField()
                #self hace referencia ala clase Post
    def __str__(self):
        return self.title