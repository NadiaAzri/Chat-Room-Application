# mysite/urls.py
from django.conf.urls import include
from django.urls import re_path
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
#from chat.views import ApproveEndorsement
urlpatterns = [
    path('chat/', include('chat.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    # re_path(r'^param$', ApproveEndorsement.as_view()),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
