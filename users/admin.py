from django.contrib import admin
from .models import ProfileUser
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField
from django import forms
from django.db import models
from modeltranslation.admin import TranslationAdmin


class UserAdminConfig(UserAdmin):
    model = ProfileUser
    search_fields = ('email', 'user_name', 'first_name',)
    list_filter = ('email', 'user_name', 'first_name', 'is_active', 'is_staff','is_superuser',)
    ordering = ('-start_date',)
    list_display = ('email','id', 'user_name', 'first_name','avatar',
                    'is_active', 'is_staff','is_superuser',)
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name','avatar',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active','is_superuser',)}),
        ('Personal', {'fields': ('about',)}),
    )
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name','avatar', 'password1', 'password2', 'is_active', 'is_staff','is_superuser',)}
         ),
    )

class ProfileUserAdmin(UserAdminConfig, TranslationAdmin):
    model = ProfileUser

# admin.site.unregister(ProfileUser)
admin.site.register(ProfileUser, ProfileUserAdmin)