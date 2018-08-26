from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.urls import reverse
from .models import UserP, Message, Comment, UserS
# Create your views here.

def new(request):
	if request.method == 'POST':

		if UserS.userManagerS.newuser(request):		# successful addition
			return redirect("/dashboard")
		else: 										# failed addition
			return redirect("/users/new")
	else:
		if 'id' not in request.session:
			messages.error(request, "Please sign in to your account to continue!")
			return redirect("/signin")
		return render(request, "users/new.html")

def editself(request):
	if 'id' not in request.session:
		messages.error(request, "Please sign in to your account to continue!")
		return redirect("/signin")


	if request.session['is_prof'] is True :
		user = UserP.userManagerP.getOneUser(request.session['id'])
	else :
		user = UserS.userManagerS.getOneUser(request.session['id'])

	context = {
		'userid':user.id,
		'email':user.email,
		'firstname':user.first_name,
		'lastname':user.last_name,
		'description':user.description,
		'userlevel':user.user_level
	}
	return render(request, "users/editself.html", context)

def editselfinfo(request):
	if request.session['is_prof'] is True :
		if UserP.userManagerP.editInfo(request):
			return redirect("/dashboard")
		else:
			return redirect("/users/edit")
	else :
		if UserS.userManagerS.editInfo(request):
			return redirect("/dashboard")
		else:
			return redirect("/users/edit")


def editselfpassword(request):
	if request.session['is_prof'] == 'True' :
		if UserP.userManagerP.editPW(request):
			return redirect("/dashboard")
		else:
			return redirect("/users/edit")
	else :
		if UserS.userManagerS.editPW(request):
			return redirect("/dashboard")
		else:
			return redirect("/users/edit")

def editselfdescription(request):
	if request.session['is_prof'] is True :
		UserP.userManagerP.editDesc(request)
		return redirect("/dashboard")
	else :
		UserS.userManagerS.editDesc(request)
		return redirect("/dashboard")

# def editother(request, user_id):
# 	if 'id' not in request.session:
# 		messages.error(request, "Please sign in to your account to continue!")
# 		return redirect("/signin")
# 	user = User.userManager.getOneUser(user_id)
# 	context = {
# 		'userid':user.id,
# 		'email':user.email,
# 		'firstname':user.first_name,
# 		'lastname':user.last_name,
# 		'userlevel':user.user_level
# 	}
# 	return render(request, "users/editother.html", context)
#
# def editotherinfo(request, user_id):
# 	if User.userManager.editInfo(request):
# 		return redirect("/dashboard")
# 	else:
# 		return redirect("/users/edit/"+user_id)
#
# def editotherpassword(request, user_id):
# 	if User.userManager.editPW(request):
# 		return redirect("/dashboard")
# 	else:
# 		return redirect("/users/edit/"+user_id)

def show(request, user_id):
	if request.method == "POST":
		if request.POST['morc'] == "message":
			Message.messageManager.addMessage(user_id, request.session['id'], request.POST['message'])
		elif request.POST['morc'] == "comment":
			Comment.commentManager.addComment(request.POST['message_id'], request.session['id'], request.POST['comment'])
		return redirect("/users/show/"+user_id)
	else:
		if 'id' not in request.session:
			messages.error(request, "Please sign in to your account to continue!")
			return redirect("/signin")
		context = Message.messageManager.getAll(request, user_id)
		return render(request, "users/show.html", context)

def destroy(request, user_id):
	
				UserS.userManagerS.deleteUser(request, user_id)
				return redirect("/dashboard")
