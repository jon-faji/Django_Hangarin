from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def root_redirect(request):
    if request.user.is_authenticated:
        return redirect('task_list')
    return redirect('account_login')

urlpatterns = [
    path('', root_redirect, name='home'),  
    path('admin/', admin.site.urls),
    path('account/', include('allauth.urls')),  
    path('tasks/', include('tasks.urls')), 
    path('', include('pwa.urls')),  
]