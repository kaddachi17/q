from django.contrib import admin
from .models import Exam,Question,Free_text,Multi_choice_answer,one_answer,Reponse
# Register your models here.
admin.site.register(Exam)

admin.site.register(Question)
admin.site.register(Free_text)
admin.site.register(Multi_choice_answer)
admin.site.register(one_answer)
admin.site.register(Reponse)
