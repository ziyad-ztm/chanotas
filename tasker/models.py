from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ToDo(models.Model):
    task = models.CharField(max_length=255)
    task_date = models.DateField()
    is_done = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)