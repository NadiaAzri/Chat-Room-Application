import random
import string
from django.contrib.auth.models import User
from .models import Contact, Message, Room
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model
User = get_user_model()


def index(request):
    return render(request, 'chat/index.html', {})


def create_room_name():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=30))

#TODO Done: securisi url taa chat room bach wahed maya9dr yodkhollo gher ida kan part of conversation, 
#TODO: room_name yetcriya auto w ukon unique,
#TODO: nraygel design (time yokhrej gedged),
#TODO: profile l kol user w hadi hamem tfenyent bach ndirha,
#TODO: login/logout/regesiter/change password/reset password,
#TODO: make the room_name in the url like this(usernamesender_usernamereviever) in a field in chat model  &&  ndir url yeddini lchaque chat ki nclicki 3liha inspkhallah
@login_required
def room(request, room_name):
    code = create_room_name()
    print(code)
    user = User.objects.get(user_name=request.user.user_name)
    contact = Contact.objects.get(user=user)
    rooms = contact.rooms.all()
    try:
        room = Room.objects.get(room_name=room_name)
        parts = room.speakers.all()
        valid = False
        for part in parts:
            if part.user == request.user:
                valid = True
                break
            else:
                valid = False
    except ObjectDoesNotExist:
        valid = False

    return render(request, 'chat/room.html', {
        'rooms': rooms,
        'room_name': room_name,
        'valid': valid,
        'username': request.user.user_name,
    })