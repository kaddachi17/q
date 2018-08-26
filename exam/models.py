from django.db import models
# from django.contrib.auth.models import User
from Authentification.models import UserP, UserS


# Create your models here.

class Exam(models.Model):
    MODE = (('TT', 'Training_Timer'),
            ('T', 'Training'),
            ('OC', 'One_try_certifie'),
            ('O', 'One_try'),
            )
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='exam_image', blank=True)
    description = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default='')
    score = models.IntegerField(default=0)
    timer = models.IntegerField(default=0)
    mode = models.CharField(max_length=1, choices=MODE, blank=True, null=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    examen = models.ForeignKey(Exam, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000, default='')
    points = models.IntegerField(default=0)
    header_text = models.CharField(max_length=1000, default='')
    footer_text = models.CharField(max_length=1000, default='')
    success_msg = models.CharField(max_length=1000, default='')
    fail_msg = models.CharField(max_length=1000, default='')

    def __str__(self):
        return self.description


class one_answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_variant = models.CharField(max_length=50)
    answer_description = models.CharField(max_length=1000)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.answer_variant


class Multi_choice_answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    multi_variant = models.CharField(max_length=50)
    multi_description = models.CharField(max_length=1000)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.multi_variant


class Free_text(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return self.text


class Reponse(models.Model):
    userS = models.ForeignKey(UserS, on_delete=models.CASCADE, blank=True, null=True)
    userP = models.ForeignKey(UserP, on_delete=models.CASCADE, blank=True, null=True)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='Exam', default=1)
    One_answer = models.ForeignKey(one_answer, on_delete=models.CASCADE, related_name='One_answer', blank=True,
                                   null=True)
    multi_choice_answer = models.ForeignKey(Multi_choice_answer, on_delete=models.CASCADE,
                                            related_name='multi_choice_answer', blank=True, null=True)
    free_text = models.CharField(max_length=1000, default='', blank=True,
                                 null=True)  # enregistrer le score ou l id!!!!!!!!!
    score_question = models.IntegerField(default=0)

# class Yard(models.Model):
# 	professor=models.ForeignKey(Profesoor,on_delete=models.CASCADE)
# 	exam=models.ForeignKey(Exam,on_delete=models.CASCADE)
