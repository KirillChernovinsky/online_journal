from django.db import models

# Create your models here.
class Estimation(models.Model):
    estimation = models.CharField(max_length=40)
    def __str__(self):
        return f'{self.estimation}'


class Object(models.Model):
    object = models.CharField(max_length=40)
    def __str__(self):
        return f'{self.object}'



class Student(models.Model):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    object = models.ForeignKey(Object, on_delete=models.CASCADE)
    estimation = models.ForeignKey(Estimation, on_delete=models.CASCADE)
    average_score = models.IntegerField()

    def __str__(self):
        return f'{self.name} {self.surname}{self.object}{self.estimation}{self.average_score}'