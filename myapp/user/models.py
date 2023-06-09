from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Tag(models.Model):
    title=models.CharField(max_length=225,unique=True)
    def __str__(self):
        return self.title

class Snippet(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    created_user = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True, blank=True,related_name="snippets")

    def __str__(self):
        return self.title
