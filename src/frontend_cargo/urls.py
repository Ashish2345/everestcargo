from django.urls import path

from .views import FrontDashView

app_name = "front_dashboard"

urlpatterns = [
    path("", FrontDashView.as_view(), name="frontdashboard")
]
