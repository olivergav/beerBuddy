from django.shortcuts import render, redirect

from .models import Room
from .forms import RoomForm


def home(request):
	rooms = Room.objects.all()
	context = {'rooms': rooms}
	return render(request, 'home/home.html', context)


def room(request, pk):
	single_room = Room.objects.get(pk=pk)
	context = {'room': single_room}
	return render(request, 'home/room.html', context)


def create_room(request):
	form = RoomForm()

	if request.method == 'POST':
		form = RoomForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home:home')

	context = {'form': form}
	return render(request, 'home/room_form.html', context)


def update_room(request, pk):
	edited_room = Room.objects.get(id=pk)
	form = RoomForm(instance=edited_room)

	if request.method == 'POST':
		form = RoomForm(request.POST, instance=edited_room)
		if form.is_valid():
			form.save()
			return redirect('home:home')

	context = {'form': form}
	return render(request, 'home/room_form.html', context)


def delete_room(request, pk):
	deleted_room = Room.objects.get(id=pk)

	if request.method == "POST":
		deleted_room.delete()
		return redirect('home:home')

	return render(request, 'home/delete.html', {'obj': deleted_room})