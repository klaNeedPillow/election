from django.db import models
from django.contrib.auth.models import User

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='candidates/', blank=True)

    def __str__(self):
        return self.name

class Vote(models.Model):
    voter = models.OneToOneField(User, on_delete=models.CASCADE) # 1 คน 1 สิทธิ์
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    voted_at = models.DateTimeField(auto_now_add=True)