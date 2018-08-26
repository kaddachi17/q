from __future__ import unicode_literals
from django.db import models

from Authentification.models import UserS, UserP
from exam.models import Exam


class Yard(models.Model):
    professor = models.ForeignKey(UserP, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    Description = models.CharField(max_length=1000, default='')
    student = models.ManyToManyField(UserS)

