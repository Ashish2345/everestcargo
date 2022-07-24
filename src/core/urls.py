from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),


    #Frontend Portion
    path("", include("frontend_cargo.urls",namespace="front_dashboard"))
]
