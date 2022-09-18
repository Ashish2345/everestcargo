from django.urls import path

from .views import (FrontDashView, ServicesView, AboutUsView, ContactUsView, BlogsView, 
                    BlogsDetailsView, TeamsView, GlobalLocationView)

app_name = "front_dashboard"

urlpatterns = [
    path("", FrontDashView.as_view(), name="frontdashboard"),
    path("services/<str:name>/", ServicesView.as_view(), name="user_services"),
    path("about_us/", AboutUsView.as_view(), name="about_us"),
    path("contact_us/", ContactUsView.as_view(), name="contact_us"),
    
    path("blogs/", BlogsView.as_view(), name="blogs"),
    path("blog_details/", BlogsDetailsView.as_view(), name="blogs_details"), 

    path("teams/", TeamsView.as_view(), name="teams"), 

    path("global_location/", GlobalLocationView.as_view(), name="location"), 




]
