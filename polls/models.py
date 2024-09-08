from django.db import models

# Create your models here.
class Question(models.Model):
    qt=models.CharField(max_length=200)
    pd=models.DateTimeField()

    def __str__(self) :
        return self.qt

class Choice(models.Model):
    q=models.ForeignKey(Question, on_delete=models.CASCADE)
    ct=models.CharField(max_length=10)
    v=models.IntegerField(default=0)

    def __str__(self) :
        return self.ct
    