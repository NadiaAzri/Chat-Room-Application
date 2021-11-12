# chat/views.py
from django.contrib.auth.models import User
from .models import Contact, Message, Room
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'chat/index.html', {})

@login_required
def room(request, room_name):
    user = User.objects.get(username=request.user.username)
    contact = Contact.objects.get(user=user)
    rooms = contact.rooms.first()
    return render(request, 'chat/room.html', {
        'rooms': rooms,
        'roomid': room_name,
        'username': request.user.username,
    })