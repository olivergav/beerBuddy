from django.contrib.auth import get_user_model
from django.db import models


class Topic(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name


class Room(models.Model):
	host = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
	topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
	name = models.CharField(max_length=200)
	description = models.TextField(null=True, blank=True)
	# participants
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name


class Message(models.Model):
	user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
	room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
	body = models.TextField(max_length=300)
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.body[0:50]
