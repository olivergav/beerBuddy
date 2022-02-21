from django.shortcuts import render

from .models import Room


def home(request):
	rooms = Room.objects.all()
	context = {'rooms': rooms}
	return render(request, 'home/home.html', context)


def room(request, pk):
	# room = None
	# for i in rooms:
	# 	if i['id'] == int(pk):
	# 		room = i
	single_room = Room.objects.get(pk=pk)
	context = {'room': single_room}
	# context = {}
	return render(request, 'home/room.html', context)
