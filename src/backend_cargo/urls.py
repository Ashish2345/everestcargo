from django.urls import path

from .views import DashboardView


app_name = "backend_dashboard"


urlpatterns = [
    
    path("profile/", DashboardView.as_view(), name="dashboard"),

]

