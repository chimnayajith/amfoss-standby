from django.db import models

class Note(models.Model):
    body = models.TextField(null=True , blank=True)
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null = True)