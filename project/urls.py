
from django.contrib import admin
from django.urls import path
from app.views import login_user,register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_user),
    path('register/', register),
]
