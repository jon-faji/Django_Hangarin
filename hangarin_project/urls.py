from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('/accounts/login/')),
    path('accounts/', include('allauth.urls')),
    path('', include('tasks.urls')),
]