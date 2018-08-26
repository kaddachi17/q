from __future__ import unicode_literals
from django.db import models
from django.contrib import messages


from Authentification.models import UserP,UserS











class MessageManager(models.Manager):
	def addMessage(self, user_to, user_from, message):
		if len(message) > 0:
			Message.objects.create(	user_to=UserS.userManagerS.get(id=user_to),
									user_from=UserP.userManagerP.get(id=user_from),
									message=message)

	def getAll (self, request, user_id):
		user = UserS.userManagerS.getOneUser(user_id)
		allMessages = Message.objects.filter(user_to=user_id).prefetch_related('comment_set').order_by('-created_at')
		context = {	'user':user,
					'allMessages':allMessages}
		return context


class Message(models.Model):
	user_to = models.ForeignKey(UserS, related_name="user_to",on_delete=models.CASCADE)
	user_from = models.ForeignKey(UserP, related_name="user_from",on_delete=models.CASCADE)
	message = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = models.Manager()
	messageManager = MessageManager()

class CommentManager(models.Manager):
	def addComment(self, message_id, user_id, comment):
		if len(comment) > 0:
			Comment.objects.create(	message=Message.objects.get(id=message_id),
									user=UserP.userManagerP.get(id=user_id),
									comment=comment)

class Comment(models.Model):
	user = models.ForeignKey(UserP,on_delete=models.CASCADE)
	message = models.ForeignKey(Message,on_delete=models.CASCADE)
	comment = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = models.Manager()
	commentManager = CommentManager()
