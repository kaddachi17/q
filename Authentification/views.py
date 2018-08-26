from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from Authentification.models import UserP
from Authentification.models import UserS

# Create your views here.
def index(request):
    if 'id' in request.session:
        if request.session['is_prof'] is True:
            user = UserP.userManagerP.getOneUser(request.session['id'])
        else:
            user = UserS.userManagerS.getOneUser(request.session['id'])

        context = {
            'is_prof': request.session['is_prof'],

        }
        return render(request, "index.html", context)
    else:
        return render(request, "index.html")


def register(request):
    if request.method == 'POST':

        if request.POST['academic'] == "professor":
            if UserP.userManagerP.register(request):  # successful registration
                return redirect("/dashboard")
            else:  # failed registration
                return redirect("/register")
        else:
            if UserS.userManagerS.register(request):  # successful registration
                return redirect("/dashboard")
            else:  # failed registration
                return redirect("/register")

    else:
        if 'id' in request.session:
            return redirect("/dashboard")
        return render(request, "registration.html")


def login(request):
    # POST
    if request.method == 'POST':
        if request.POST['academic'] == 'professor':
            if UserP.userManagerP.login(request):  # successful login
                return redirect("/dashboard")
            else:  # failed login
                return redirect("/signin")
        elif request.POST['academic'] == 'student':
            if UserS.userManagerS.login(request):  # successful login
                return redirect("/dashboard")
            else:  # failed login
                return redirect("/signin")
        else:  # failed login
            return redirect("/signin")
    # GET
    else:
        if 'id' in request.session:
            return redirect("/dashboard")
        return render(request, "login.html")


def logoff(request):
    if request.session['is_prof'] is True:
        UserP.userManagerP.logoff(request)  # failed login
        return redirect("/")
    else:
        UserS.userManagerS.logoff(request)  # failed login
        return redirect("/")
