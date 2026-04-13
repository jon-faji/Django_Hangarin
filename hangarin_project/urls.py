from django.contrib import admin
from django.urls import path

urlpatterns = [
    # =========================
    # ADMIN
    # =========================
    path('admin/', admin.site.urls),
]
