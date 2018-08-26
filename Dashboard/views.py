from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .models import UserP, UserS
from exam.models import Exam
from .models import Yard


# from .models import User
# Create your views here.

def dashboard(request):
    if 'id' not in request.session:
        messages.error(request, "Please sign in to your account to continue!")
        return redirect("/signin")
    if request.session['is_prof'] is True:
        professor = UserP.userManagerP.getOneUser(request.session['id'])
        all_my_students = professor.student.all()
        context = {
            'all_my_students': all_my_students,
            'all_students': UserS.userManagerS.getAllUsers(),
            'professor': UserP.userManagerP.getOneUser(request.session['id']),
            'is_prof': request.session['is_prof'],
        }
        return render(request, "dashboard.html", context)
    if request.session['is_prof'] == False:
        return redirect("/exam/")


def affectexam(request):
    all_users = UserS.userManagerS.getAllUsers()
    all_exam = Exam.objects.all()
    if 'id' not in request.session:
        messages.error(request, "Please sign in to your account to continue!")
        return redirect("/signin")
    if request.method == 'POST':
        if request.session['is_prof'] is True:
            yard = Yard()

            yard.professor = UserP.userManagerP.getOneUser(request.session['id'])
            id_exam = request.POST['selected']
            yard.exam = Exam.objects.get(pk=id_exam)
            yard.save()
            choice1 = request.POST.getlist('hisstudent')
            choice2 = request.POST.getlist('allstudent')

            for item in choice1:
                yard.student.add(UserS.objects.get(pk=item))
            for item1 in choice2:
                yard.student.add(UserS.objects.get(pk=item1))
            yard.save()
            context = {
                'all_users': all_users,
                'all_exam': all_exam,
                'professor': UserP.userManagerP.getOneUser(request.session['id']),
                'is_prof': request.session['is_prof'],
            }
            return render(request, "createyard.html", context)
    else:
        context = {
            'all_users': all_users,
            'all_exam': all_exam,
            'professor': UserP.userManagerP.getOneUser(request.session['id']),
            'is_prof': request.session['is_prof'],
        }
        return render(request, "createyard.html", context)


def addstudent(request, user_id):
    professor = UserP.userManagerP.getOneUser(request.session['id'])
    student_to_add = UserS.userManagerS.getOneUser(user_id)
    if student_to_add not in professor.student.all():
        professor.student.add(student_to_add)
    else:
        return redirect("/dashboard/")
    return redirect("/dashboard/")


def removestudent(request, user_id):
    professor = UserP.userManagerP.getOneUser(request.session['id'])
    student_to_add = UserS.userManagerS.getOneUser(user_id)
    professor.student.remove(student_to_add)
    return redirect("/dashboard/")
