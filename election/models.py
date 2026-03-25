from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField(unique=True)
    policy = models.TextField()

    def __str__(self):
        return f"{self.number}: {self.name}"

class Vote(models.Model):
    candidate = models.ForeignKey(Candidate, on_object=models.CASCADE)
    voter_name = models.CharField(max_length=50) 
    voted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('voter_name',) 