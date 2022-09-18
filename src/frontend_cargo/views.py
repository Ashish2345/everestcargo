from django.shortcuts import render
from django.views import View

class FrontDashView(View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = "user_dashboard.html"
        self.args = {}
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class ServicesView(View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = "services.html"
        self.args = {}
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        name = kwargs.get("name")
        self.args = {
            "page_name":name
        }

        return render(request, self.template_name, self.args)

class AboutUsView(View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = "about_us.html"
        self.args = {}
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.args = {
            "page_name":"About Us"
        }
        return render(request, self.template_name, self.args)


class ContactUsView(View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = "contact_us.html"
        self.args = {}
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.args = {
            "page_name":"Contact Us"
        }
        return render(request, self.template_name, self.args)

class BlogsView(View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = "blogs.html"
        self.args = {}
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.args = {
            "page_name":"Blog"
        }
        return render(request, self.template_name, self.args)

class BlogsDetailsView(View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = "blog_details.html"
        self.args = {}
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.args = {
            "page_name":"Blog Details"
        }
        return render(request, self.template_name, self.args)

class TeamsView(View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = "teams.html"
        self.args = {}
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.args = {
            "page_name":"Teams"
        }
        return render(request, self.template_name, self.args)

class GlobalLocationView(View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = "global_location.html"
        self.args = {}
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.args = {
            "page_name":"Locations"
        }
        return render(request, self.template_name, self.args)