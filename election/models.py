from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField(unique=True)
    policy = models.TextField()

    def __str__(self):
        return f"{self.number}: {self.name}"

class Vote(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    session_id = models.CharField(max_length=100) # เก็บ ID ของ Browser นั้นๆ
    voted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('session_id',) # 1 Session โหวตได้ครั้งเดียว