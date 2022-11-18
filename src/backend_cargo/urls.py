from django.urls import path

from .views import (DashboardView, OverviewView, AboutUsView, TeamsView, ServicesView, TrackingView, 
                    BlogView,TestimonialView,TestimonialEditView, TestimonialDeleteView, BlogDetailsView,BlogEditView, BlogDeleteView, EcommerceView, SystemSettingView, ConatctUsView, 
                    TrackingStatsChangeView, TeamsDeleteView,TrackingDeleteView,PackageAddView,PackageDeleteView, TrackingEditView, PackageEditView,PackageView,QuotesView,QuotesDetailView, ServiceView, TeamsDetailsView, FAQView, FAQEditView, FAQDeleteView)


app_name = "backend_dashboard"


urlpatterns = [
    
    path("profile/", DashboardView.as_view(), name="dashboard"),
    path("overview/", OverviewView.as_view(), name="overview"),
    path("about_us/", AboutUsView.as_view(), name="about_us"),
    path("contact_us/", ConatctUsView.as_view(), name="contact_us_admin"),
    
    path("teams/", TeamsView.as_view(), name="teams_admin"),
    path("teams/<int:id>", TeamsDetailsView.as_view(), name="teams_details"),
    path("teams/delete/<int:id>", TeamsDeleteView.as_view(), name="teams_delete"),
    
    path("services/", ServicesView.as_view(), name="services"),
    path("tracking/", TrackingView.as_view(), name="tracking"),
    
    path("blog/", BlogView.as_view(), name="blog"),
    path("blog/<int:id>", BlogDetailsView.as_view(), name="blog_details"),
    path("blog/edit/<int:id>", BlogEditView.as_view(), name="blog_edit"),
    path("blog/delete/<int:id>", BlogDeleteView.as_view(), name="blog_delete"),
    
    path("testimonials/", TestimonialView.as_view(), name="testimonials"),
    path("testimonials/edit/<int:id>", TestimonialEditView.as_view(), name="testimonials_edit"),
    path("testimonials/delete/<int:id>", TestimonialDeleteView.as_view(), name="testimonials_delete"),


    path("faq/", FAQView.as_view(), name="faq_admin"),
    path("faq/edit/<int:id>", FAQEditView.as_view(), name="faq_edit"),
    path("faq/delete/<int:id>", FAQDeleteView.as_view(), name="faq_delete"),

    path("service/<str:servicetag>", ServiceView.as_view(), name="service_view"),

    path("quotes/", QuotesView.as_view(), name="quotes_admin"),
    path("quotes/<int:id>", QuotesDetailView.as_view(), name="quotes_detail_admin"),


    path("package/", PackageView.as_view(), name="package_admin"),
    path("package/add", PackageAddView.as_view(), name="package_add"),

    path("package/edit/<int:id>", PackageEditView.as_view(), name="package_edit"),
    path("package/delete/<int:id>", PackageDeleteView.as_view(), name="package_delete"),

    path("tracking/", TrackingView.as_view(), name="tracking_admin"),
    path("tracking/edit/<int:id>", TrackingEditView.as_view(), name="tracking_edit_admin"),
    path("tracking/delete/<int:id>", TrackingDeleteView.as_view(), name="tracking_delete_admin"),

    
    path("change_Status/tracking", TrackingStatsChangeView.as_view(), name="tracking_change"),
    path("ecommerce/", EcommerceView.as_view(), name="ecommerce"),
    path("system_setting/", SystemSettingView.as_view(), name="system_setting"),




]

