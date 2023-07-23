from django.urls import path

from .views import (FrontDashView, ServicesView, AboutUsView, ContactUsView, BlogsView, 
                    BlogsDetailsView,ComingSoonView,ProductsDetailsView,ProductsView,PrivacyPolicyView,TermsandConditionView, TrackingDetailsView, RequestQuotesView, TeamsView, GlobalLocationView, TrackingView)

app_name = "front_dashboard"

urlpatterns = [
    path("", FrontDashView.as_view(), name="frontdashboard"),
    path("services/<str:name>/", ServicesView.as_view(), name="user_services"),
    path("about_us/", AboutUsView.as_view(), name="about_us"),
    path("contact_us/", ContactUsView.as_view(), name="contact_us"),
    
    path("blogs/", BlogsView.as_view(), name="blogs"),
    path("blog_details/<int:id>/", BlogsDetailsView.as_view(), name="blogs_details"), 

    path("teams/", TeamsView.as_view(), name="teams"), 
    path("products/", ProductsView.as_view(), name="products"), 
    path("products/details/<int:id>/", ProductsDetailsView.as_view(), name="products-deails"), 

    path("global_location/", GlobalLocationView.as_view(), name="location"), 

    #tracking
    path("tracking/", TrackingView.as_view(), name="tracking_package"), 
    path("tracking/awb/", TrackingDetailsView.as_view(), name="tracking_details"), 

    #quotes
    path("request/quotes/", RequestQuotesView.as_view(), name="request_quotes"), 

    path("privacy_policy/", PrivacyPolicyView.as_view(), name="privacy_policy"), 
    path("comingsoon/", ComingSoonView.as_view(), name="comingsoon"), 


    path("termsandcondition/", TermsandConditionView.as_view(), name="termsandcondition"), 




]
