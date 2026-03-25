from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField(unique=True) # เบอร์ผู้สมัคร
    policy = models.TextField() # นโยบาย

    def __str__(self):
        return f"{self.number}: {self.name}"