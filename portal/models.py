from django.contrib.auth.models import AbstractUser
from django.db import models
GRADE = (('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F'))
COMMENT = (('pass', 'Pass'), ('fail', 'Fail'))


class Emmamodel(models.Model):
    first_test = models.IntegerField()
    second_test = models.IntegerField()
    total_test = models.IntegerField()
    exam = models.IntegerField()
    total = models.IntegerField()
    grade = models.CharField(max_length=10, choices=GRADE)
    comment = models.CharField(max_length=10, choices=COMMENT)

    def __str__(self):
        return self.comment


class Christymodel(models.Model):
    first_test = models.IntegerField()
    second_test = models.IntegerField()
    total_test = models.IntegerField()
    exam = models.IntegerField()
    total = models.IntegerField()
    grade = models.CharField(max_length=10, choices=GRADE)
    comment = models.CharField(max_length=10, choices=COMMENT)

    def __str__(self):
        return self.comment


class Robmodel(models.Model):
    first_test = models.IntegerField()
    second_test = models.IntegerField()
    total_test = models.IntegerField()
    exam = models.IntegerField()
    total = models.IntegerField()
    grade = models.CharField(max_length=10, choices=GRADE)
    comment = models.CharField(max_length=10, choices=COMMENT)

    def __str__(self):
        return self.comment


class Imomodel(models.Model):
    first_test = models.IntegerField()
    second_test = models.IntegerField()
    total_test = models.IntegerField()
    exam = models.IntegerField()
    total = models.IntegerField()
    grade = models.CharField(max_length=10, choices=GRADE)
    comment = models.CharField(max_length=10, choices=COMMENT)

    def __str__(self):
        return self.comment
