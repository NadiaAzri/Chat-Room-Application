from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from . import forms
import random
import string
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from chat.models import Contact, Room,Message
from django.contrib.auth import get_user_model
User = get_user_model()


def create_room_name():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=30))


class SignupView(FormView):
    """sign up user view"""
    form_class = forms.SignupForm
    template_name = 'chat/signup.html'
    # success_url = reverse_lazy('chat:room', kwargs={'room_name': room_name})
    # def get_success_url(self, room_name):
    #       # if you are passing 'pk' from 'urls' to 'DeleteView' for company
    #       # capture that 'pk' as companyid and pass it to 'reverse_lazy()' function
    #     #   companyid=self.kwargs['pk']
    #       return reverse_lazy('chat:room', kwargs={'room_name': room_name})
    def form_valid(self, form):
        """ process user signup"""
        user = form.save(commit=False)
        user.save()

        admin = User.objects.get(user_name='admin')
        contact = Contact.objects.create(user=user)
        contact_admin = Contact.objects.get(user=admin)
        contact_admin.friends.add(contact)
        # room_name = 'admin' + str(user.user_name)
        room_name = create_room_name()
        room = Room.objects.create(name='Our App',room_name= room_name)
        room.speakers.add(contact)
        room.speakers.add(contact_admin)
        message = Message.objects.create(contact=contact_admin, content='Hello, This is the Admin', chat=room)
        
        login(self.request, user)
        if user is not None:
            return redirect('chat:room', room_name)
            # return HttpResponseRedirect(self.success_url)

        return super().form_valid(form)

def Logout(request):
    """logout logged in user"""
    logout(request)
    return HttpResponseRedirect(reverse_lazy('custom_auth:login'))


class LoginView(FormView):
    """login view"""

    form_class = forms.LoginForm
    #success_url = reverse_lazy('chat:index')
    template_name = 'chat/login.html'

    def form_valid(self, form):
        """ process user login"""
        credentials = form.cleaned_data

        user = authenticate(username=credentials['email'],
                            password=credentials['password'])

        if user is not None:
            login(self.request, user)
            user = User.objects.get(user_name=user.user_name)
            contact = Contact.objects.get(user=user)
            room = contact.rooms.last()
            room_name = room.room_name
            return redirect('chat:room', room_name)
            # return HttpResponseRedirect(self.success_url)

        else:
            messages.add_message(self.request, messages.INFO, 'Wrong credentials\
                                please try again')
            return HttpResponseRedirect(reverse_lazy('custom_auth:login'))


