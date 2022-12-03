from django.shortcuts import render
from django.views import View
from backend_cargo.models import *
from django.http import HttpResponseRedirect
from backend_cargo.forms import ContactUsModelForm
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


class FrontDashView(View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = "user_dashboard.html"
        self.args = {}
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        about_us = AboutUsModel.objects.first()
        faq_model = FAQModel.objects.all()[::3]
        testimonials = TestimonialsModel.objects.all()[::4]
        blogs = BlogModel.objects.all()[::6]
        self.args = {
            "about_us":about_us,
            "faq_model":faq_model,
            "testimonials":testimonials,
            "blogs":blogs
        }
        return render(request, self.template_name, self.args)



class ServicesView(View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = "services.html"
        self.args = {}
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        name = kwargs.get("name")
        try:
            service_details = ServiceModel.objects.filter(tag_name=name).latest()
        except:
            service_details = []
        self.args = {
            "page_name":name,
            "service_details":service_details
        }

        return render(request, self.template_name, self.args)

class AboutUsView(View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = "about_us.html"
        self.args = {}
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        about_us = AboutUsModel.objects.first()
        self.args = {
            "page_name":"About Us",
            "about_us":about_us
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

    def post(self, request):
        contact_details = request.POST.dict()
        form = ContactUsModelForm(data={**contact_details})
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))



class BlogsView(View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = "blogs.html"
        self.args = {}
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        all_blogs = BlogModel.objects.all()

        paginator = Paginator(all_blogs, 6)
        page = request.GET.get('page')
        paged_blogs = paginator.get_page(page)
        self.args = {
            "page_name":"Blog",
            "all_blog":paged_blogs
        }
        return render(request, self.template_name, self.args)

class BlogsDetailsView(View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = "blog_details.html"
        self.args = {}
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):

        blog_id = kwargs.get("id")
        blog_details = BlogModel.objects.get(id=blog_id)
        self.args = {
            "page_name":"Blog Details",
            "blog_details":blog_details
        }
        return render(request, self.template_name, self.args)

class TeamsView(View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = "teams.html"
        self.args = {}
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        all_teams = Teams.objects.all()
        self.args = {
            "page_name":"Teams",
            "all_teams":all_teams
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


class TrackingView(View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = "tracking.html"
        self.args = {}
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.args = {
            "page_name":"Tracking"
        }
        return render(request, self.template_name, self.args)


class TrackingDetailsView(View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = "tracking_detail.html"
        self.args = {}
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        track_num = request.GET.get("awb_no")
        qs = TrackingModel.objects.get(tracking_code=track_num)
        print(track_num)
        self.args = {
            "qs":qs,
            "page_name":"Tracking Details"
        }
        return render(request, self.template_name, self.args)




class RequestQuotesView(View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = "quote.html"
        self.args = {}
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.args = {
            "page_name":"Request a quote"
        }
        return render(request, self.template_name, self.args)
