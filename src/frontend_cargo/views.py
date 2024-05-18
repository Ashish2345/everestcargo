from django.shortcuts import render
from django.views import View
from backend_cargo.models import *
from django.http import HttpResponseRedirect
from backend_cargo.forms import ContactUsModelForm
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views.generic import TemplateView
from django.contrib import messages

class FrontDashView(View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = "user_dashboard.html"
        self.args = {}
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        about_us = AboutUsModel.objects.first()
        faq_model = FAQModel.objects.all()
        testimonials = TestimonialsModel.objects.all()
        blogs = BlogModel.objects.order_by("-created_date")[:3]
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
            service_details = ServiceModel.objects.filter(tag_name=name).first()
        except:
            service_details = []
        self.args = {
            "img_url":"/django-static/img/cargo_img/ser.png",    
            "page_name":service_details.service_name,
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
            "about_us":about_us,
            "img_url":"/django-static/img/cargo_img/about_us.jpg",    
        }
        return render(request, self.template_name, self.args)

import urllib, json
def validate_captcha(request):
    recaptcha_response = request.POST.get('g-recaptcha-response')
    url = 'https://www.google.com/recaptcha/api/siteverify'
    values = { 
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
            }
    
    data = urllib.parse.urlencode(values).encode()
    req =  urllib.request.Request(url, data=data)
    response = urllib.request.urlopen(req)
    result = json.loads(response.read().decode())
    
    return result


class ContactUsView(View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = "contact_us.html"
        self.args = {}
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.args = {
            "page_name":"Contact Us",
             "img_url":"/django-static/img/cargo_img/contact_us.jpg",    
        }
        return render(request, self.template_name, self.args)

    def post(self, request):
        result = validate_captcha(request)
        if result["success"] != True:
            messages.error(request, 'Invalid Captcha!!')
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

        contact_details = request.POST.dict()
        form = ContactUsModelForm(data={**contact_details})
        if form.is_valid():
            form.save()
            messages.success(request, 'Message successfully send!!')

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
            "all_blog":paged_blogs,
            "img_url":"/django-static/img/cargo_img/blog_i.jpg",
        }
        return render(request, self.template_name, self.args)

class BlogsDetailsView(View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = "blog_details.html"
        self.args = {}
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        all_blogs = BlogModel.objects.all().order_by("-created_date")

        blog_id = kwargs.get("id")
        blog_details = BlogModel.objects.get(id=blog_id)
        comment = CommentModel.objects.filter(blog=blog_details)
        self.args = {
            "page_name":"Blog Details",
            "blog_details":blog_details,
            "img_url":"/django-static/img/cargo_img/blog_i.jpg",
            "comment":comment,
            "comment_count":comment.count(),
            "all_blogs":all_blogs
        }
        return render(request, self.template_name, self.args)

    def post(self, request, *args, **kwargs):

        blog_id = kwargs.get("id")
        blog_details = BlogModel.objects.get(id=blog_id)
        CommentModel.objects.create(blog=blog_details,creater_name=request.POST.get('name'),creater_email=request.POST.get('email'),comment=request.POST.get('message') )
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

class TeamsView(View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = "teams.html"
        self.args = {}
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        all_teams = Teams.objects.all()
        self.args = {
            "page_name":"Teams",
            "img_url":"/django-static/img/cargo_img/5471.jpg",
            "all_teams":all_teams
        }
        return render(request, self.template_name, self.args)


class ProductsView(View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = "products.html"
        self.args = {}
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.args = {
            "page_name":"Products",
            "img_url":"/django-static/img/eccom.jpg",
            "products": Ecommerce.objects.all()
        }
        return render(request, self.template_name, self.args)

from .forms import CheckoutInquiryForm

class ProductsDetailsView(View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = "product_details.html"
        self.args = {}
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        id = self.kwargs.get("id")
        product_Det = Ecommerce.objects.get(id=id)
        other_products = Ecommerce.objects.exclude(id=id)
        self.args = {
            "page_name":"Product Details",
            "img_url":"/django-static/img/eccom.jpg",
            "product_Det":product_Det,
            "other_products":other_products,
            "form": CheckoutInquiryForm()
            
        }
        return render(request, self.template_name, self.args)

    def post(self, request, *args, **kwargs):
        id = self.kwargs.get("id")
        product_Det = Ecommerce.objects.get(id=id)
        data_dict = request.POST.dict()
        form = CheckoutInquiryForm(data = {**data_dict})
        if form.is_valid():
            quantity = request.POST.get("quantity", 0)
            m = form.save(commit=False)
            m.product = product_Det
            m.quantity = int(quantity)
            m.save()

            self.args = {"success": "Order send for inquiry!!",
                         "page_name":"Product Details",
                        "img_url":"/django-static/img/eccom.jpg",
                        "product_Det":product_Det,
                        "other_products":Ecommerce.objects.exclude(id=id),
                        "form": CheckoutInquiryForm()}
            return render(request, self.template_name, self.args)


class GlobalLocationView(View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = "global_location.html"
        self.args = {}
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.args = {
            "page_name":"Locations",
            "img_url":"/django-static/img/cargo_img/global-communication-background-business-network-design.jpg",
        }
        return render(request, self.template_name, self.args)


class TrackingView(View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = "tracking.html"
        self.args = {}
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.args = {
            "page_name":"Tracking",
             "img_url":"/django-static/img/cargo_img/abnner.jpg",    
        }
        return render(request, self.template_name, self.args)


class TrackingDetailsView(View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = "tracking_detail.html"
        self.args = {}
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        track_num = request.GET.get("awb_no")
        try:
            qs = TrackingModel.objects.get(tracking_code=track_num)
        except: 
            qs = None
        self.args = {
            "qs":qs,
            "page_name":"Tracking Details",
            "img_url":"/django-static/img/cargo_img/abnner.jpg", 
        }
        if qs is None:
            return render(request,"tracking.html",{"message":"Your tracking number doesnot match!!", "page_name":"Tracking Details",  "img_url":"/django-static/img/cargo_img/abnner.jpg"} )

        return render(request, self.template_name, self.args)




class RequestQuotesView(View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = "quote.html"
        self.args = {}
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.args = {
            "courier": CourierModel.objects.all(),
            "page_name":"Request a quote",
            "img_url":"/django-static/img/cargo_img/quor.jpg", 
        }

        
        return render(request, self.template_name, self.args)

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")

        email = request.POST.get("email")
        phone = request.POST.get("phone")
        freight = int(request.POST.get("freight"))
        country = request.POST.get("country")
        city = request.POST.get("city")
        width = request.POST.get("width")
        Height = request.POST.get("Height")
        weight = request.POST.get("weight")
        length = request.POST.get("length")
        freights = CourierModel.objects.get(id=freight)
        m = GetQuote(full_name=name, email=email, phone=phone,country=country,city_departure=city,width=width, height=Height, weight=weight, length=length  )
        m.flight_type = freights
        m.save()
        messages.success(request, 'Quote Successfully Created!!')

        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

class PrivacyPolicyView(TemplateView):
    template_name = "privacypolicy.html"
    def get_context_data(self,*args, **kwargs):
        context = super(PrivacyPolicyView, self).get_context_data(*args,**kwargs)
        context['page_name'] = "Privacy Policy"
        context['img_url'] = "/django-static/img/cargo_img/privacy.jpg"

        return context

class TermsandConditionView(TemplateView):
    template_name = "termsandcondition.html"
    def get_context_data(self,*args, **kwargs):
        context = super(TermsandConditionView, self).get_context_data(*args,**kwargs)
        context['page_name'] = "Terms and Condition"
        context['img_url'] = "/django-static/img/cargo_img/terms.jpg"

        return context


class ComingSoonView(TemplateView):
    template_name = "comming_soon.html"
