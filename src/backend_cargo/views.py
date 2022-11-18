
from django.shortcuts import redirect, render
from django.views import View   
from django.http import HttpResponseRedirect

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib import messages

from .forms import TestimonialsModelForm,PackageModelForm, TrackingModelForm, ServiceModelForm,ShipperModelForm,ReceiverModelForm, FAQModelForm, UserLoginForm, TeamsForm,BlogForm, OverviewBannerModelForm, AboutModelForm, SiteOptionUpdateForm, SystemSettingsUpdateForm

from .models import (Profile, GetQuote,OverviewBannerModel, AboutUsModel, ContactUsModel, Teams, SiteSetting, SystemSettings, BlogModel, CommentModel, 
                    PackageModel,TrackingStatus, TrackingModel,PackageDetailsModel, TestimonialsModel, FAQModel, ServiceModel)

class DashboardView(LoginRequiredMixin, View):
    def get(self, request):
        profile_qs = Profile.objects.get(user=request.user)  
        self.args={
            "profile_qs":profile_qs,
            "heading": "Dashboard",
            "pageview":"Dashboard"
        }
        return render(request, 'dashboard.html',self.args)


class OverviewView(LoginRequiredMixin, View):

    def dispatch(self, request, *args, **kwargs):
        self.template_name = "overview.html"
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        qs = OverviewBannerModel.objects.first()
        self.args={
            "heading": "Overview",
            "form": OverviewBannerModelForm(instance=qs),
            "qs":qs
        }
        return render(request, self.template_name,self.args)

    def post(self, request):
        qs = OverviewBannerModel.objects.first()
        banner = request.FILES.get("banner")
        form = OverviewBannerModelForm(request.POST, instance=qs)
        if form.is_valid():
            a = form.save(commit=False)
            if banner:
                a.banner_image = banner
            a.save()
            messages.success(request, "OverView Banner Updated Successfully!!")
        else:
            messages.error(request, "OverView Banner unable to update!!")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


class AboutUsView(LoginRequiredMixin, View):

    def dispatch(self, request, *args, **kwargs):
        self.template_name = "about_us_admin.html"
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        qs = AboutUsModel.objects.first()
        self.args={
            "heading": "About Us",
            "form": AboutModelForm(instance=qs),
            "qs":qs
        }
        return render(request, self.template_name ,self.args)

    def post(self, request):
        qs = AboutUsModel.objects.first()
        banner = request.FILES.get("banner")
        form = AboutModelForm(request.POST, instance=qs)
        if form.is_valid():
            a = form.save(commit=False)
            if banner:
                a.banner_image = banner
            a.save()
            messages.success(request, "OverView Banner Updated Successfully!!")
        else:
            messages.error(request, "OverView Banner unable to update!!")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


class ConatctUsView(LoginRequiredMixin, View):

    def dispatch(self, request, *args, **kwargs):
        self.template_name = "contact_us_admin.html"
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        qs = ContactUsModel.objects.all().order_by("created_date")
        self.args={
            "heading": "Contact Us",
            "contact_lists":qs
        }
        return render(request, self.template_name ,self.args)


class TeamsView(LoginRequiredMixin, View):

    def dispatch(self, request, *args, **kwargs):
        self.template_name = "teams_admin.html"
        return super().dispatch(request, *args, **kwargs)


    def get(self, request):
        qs = Teams.objects.all().order_by("id")
        form = TeamsForm()
        self.args={
            "heading": "Teams",
            "team_lists":qs,
            "form":form
        }
        return render(request,  self.template_name ,self.args)

    def post(self, request):
        user_image = request.FILES.get("user_image")
        form = TeamsForm(request.POST,request.FILES )
        if form.is_valid():
            a = form.save(commit=False)
            if user_image:
                a.user_image = user_image
            a.save()
            messages.success(request, "Teams Added Successfully Successfully!!")
        else:
            messages.error(request, "Unable to add users!!")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

class TeamsDetailsView(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = "team_details.html"
        return super().dispatch(request, *args, **kwargs)


    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        qs = Teams.objects.get(id=id)
        form = TeamsForm(instance=qs)
        self.args={
            "heading": "Team Details",
            "team_lists":qs,
            "form":form
        }
        return render(request,  self.template_name ,self.args) 

    def post(self, request, *args, **kwargs):
        id = kwargs.get("id")
        qs = Teams.objects.get(id=id)
        user_image = request.FILES.get("user_img")
        form = TeamsForm(request.POST, request.FILES, instance=qs)
        if form.is_valid():
            a = form.save(commit=False)
            if user_image:
                a.user_image = user_image
            a.save()
            messages.success(request, "User Updated Successfully!!")
        else:
            messages.error(request, "User unable to update!!")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


class TeamsDeleteView(LoginRequiredMixin, View):
     def post(self, request, *args, **kwargs):
        id = kwargs.get("id")
        Teams.objects.get(id=id).delete()
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


class ServicesView(LoginRequiredMixin, View):
    def get(self, request):
        self.args={
            "heading": "Overview"
        }
        return render(request, 'overview.html',self.args)


class TrackingView(LoginRequiredMixin, View):
    def get(self, request):
        self.args={
            "heading": "Overview"
        }
        return render(request, 'overview.html',self.args)


class BlogView(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = "blogs_setup.html"
        return super().dispatch(request, *args, **kwargs)


    def get(self, request):
        qs = BlogModel.objects.all().order_by("id")
        self.args={
            "heading": "Blogs",
            "blogs_lists":qs,
            "form":BlogForm()
        }
        return render(request,  self.template_name ,self.args)

    def post(self, request, *args, **kwargs):
        blog_image = request.FILES.get("blog_image")
        sub_image1 = request.FILES.get("sub_image1")
        sub_image2 = request.FILES.get("sub_image2")
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            a = form.save(commit=False)
            a.blog_image = blog_image
            a.sub_image1 = sub_image1
            a.sub_image2 = sub_image2
            a.created_by = request.user
            a.save()
            messages.success(request, "Blog Added Successfully!!")
        else:
            messages.error(request, "Unable to add blog!!")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


class BlogDetailsView(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = "blog_details_admin.html"
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        qs = BlogModel.objects.get(id=id)
        comments_related = CommentModel.objects.filter(blog=qs)
        print(comments_related)
        # form = TeamsForm(instance=qs)
        self.args={
            "heading": "Blog Details",
            "blog":qs,
            "comments_related":comments_related
            # "form":form
        }
        return render(request,  self.template_name ,self.args) 

    def post(self, request, *args, **kwargs):
        id = kwargs.get("id")
        qs = BlogModel.objects.get(id=id)
        CommentModel.objects.create(blog=qs,title=request.POST.get("your_title"),creater_name=request.POST.get("your_name"),creater_email=request.POST.get("your_email"),comment=request.POST.get("your_message"))
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))



class BlogEditView(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = "blogs_edit.html"
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        qs = BlogModel.objects.get(id=id)
        self.args = {
            "heading": qs.title,
            "form":BlogForm(instance=qs),
            "qs":qs
        }
        return render(request,  self.template_name ,self.args) 

    def post(self, request, *args, **kwargs):
        id = kwargs.get("id")
        qs = BlogModel.objects.get(id=id)
        blog_image = request.FILES.get("blog_image","")
        sub_image1 = request.FILES.get("sub_image1","")
        sub_image2 = request.FILES.get("sub_image2","")
        form = BlogForm(request.POST,request.FILES, instance=qs)
        if form.is_valid():
            a = form.save(commit=False)
            if blog_image != "":
                a.blog_image = blog_image
            if sub_image1 != "":
                a.sub_image1 = sub_image1
            if sub_image2 != "":
                a.sub_image2 = sub_image2
            a.created_by = request.user
            a.save()
            messages.success(request, "Blog Updated Successfully!!")
        else:
            messages.error(request, "Unable to update blog!!")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

class BlogDeleteView(LoginRequiredMixin, View):
     def post(self, request, *args, **kwargs):
        id = kwargs.get("id")
        BlogModel.objects.get(id=id).delete()
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


class EcommerceView(LoginRequiredMixin, View):
    def get(self, request):
        self.args={
            "heading": "Overview"
        }
        return render(request, 'overview.html',self.args)


class SystemSettingView(LoginRequiredMixin, View):

    def dispatch(self, request, *args, **kwargs):
        self.template_name = "site_settings.html"
        return super().dispatch(request, *args, **kwargs)


    def get(self, request):
        site_option_qs = SiteSetting.objects.first()
        system_option_qs = SystemSettings.objects.first()
        siteupdate_form = SiteOptionUpdateForm(instance=site_option_qs)
        systemupdate_form = SystemSettingsUpdateForm(instance=system_option_qs)
        self.args={
            "heading": "Site Settings",
            "site_option_qs":site_option_qs,
            "system_option_qs":system_option_qs,
            "siteupdate_form":siteupdate_form,
            "systemupdate_form":systemupdate_form
        }
        return render(request, self.template_name,self.args)

    def post(self, request):
        if "site_settings" in request.POST:
            qs = SiteSetting.objects.first()
            logo = request.FILES.get("logo")
            favicon = request.FILES.get("favicon")       
            form = SiteOptionUpdateForm(request.POST, instance=qs)
            if form.is_valid():
                print(222222)
                a = form.save(commit=False)
                if logo:
                    a.logo_image = logo
                if favicon:
                    a.favicon = favicon
                a.save()
                messages.success(request, "Site Settings Updated Successfully!!")
            else:
                messages.error(request, "Site Settings unable to update!!")
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
        else:
            qs = SystemSettings.objects.first()      
            form = SystemSettingsUpdateForm(request.POST, instance=qs)
            if form.is_valid():
                form.save()
                messages.success(request, "System Settings Updated Successfully!!")
            else:
                messages.error(request, "System Settings unable to update!!")
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


class TestimonialView(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = "testimonials.html"
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        qs = TestimonialsModel.objects.all().order_by("id")
        self.args={
            "heading": "Testimonials",
            "testimonials":qs,
            "form":TestimonialsModelForm()
        }
        return render(request,  self.template_name ,self.args)

    def post(self, request, *args, **kwargs):
        testimonials_image = request.FILES.get("testimonials_image")

        form = TestimonialsModelForm(request.POST, request.FILES)
        if form.is_valid():
            a = form.save(commit=False)
            a.user_image = testimonials_image
            a.save()
            messages.success(request, "Testimonials Added Successfully!!")
        else:
            messages.error(request, "Unable to add testimonials!!")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


class TestimonialEditView(LoginRequiredMixin, View):

    def dispatch(self, request, *args, **kwargs):
        self.template_name = "testimonials_edit.html"
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        qs = TestimonialsModel.objects.get(id=id)
        self.args={
            "heading": "Edit Testimonials",
            "form": TestimonialsModelForm(instance=qs),
            "qs":qs
        }
        return render(request, self.template_name,self.args)

    def post(self, request, *args, **kwargs):
        id = kwargs.get("id")
        qs = TestimonialsModel.objects.get(id=id)
        user_image = request.FILES.get("user_image","")
        form = TestimonialsModelForm(request.POST,request.FILES, instance=qs)
        if form.is_valid():
            a = form.save(commit=False)
            if user_image != "":
                a.user_image = user_image
            a.save()
            messages.success(request, "Testimonials Updated Successfully!!")
        else:
            messages.error(request, "Testimonials unable to update!!")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


class TestimonialDeleteView(LoginRequiredMixin, View):
     def post(self, request, *args, **kwargs):
        id = kwargs.get("id")
        TestimonialsModel.objects.get(id=id).delete()
        messages.success(request, "Testimonials Deleted Successfully!!")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))



class FAQView(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = "faq.html"
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        qs = FAQModel.objects.all().order_by("id")
        self.args={
            "heading": "Frequently Asked Question",
            "all_faq":qs,
            "form":FAQModelForm()
        }
        return render(request,  self.template_name ,self.args)

    def post(self, request, *args, **kwargs):
        form = FAQModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "FQA Added Successfully!!")
        else:
            messages.error(request, "Unable to add FQA!!")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


class FAQEditView(LoginRequiredMixin, View):

    def dispatch(self, request, *args, **kwargs):
        self.template_name = "faq_edit.html"
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        qs = FAQModel.objects.get(id=id)
        self.args={
            "heading": "Edit FAQ",
            "form": FAQModelForm(instance=qs),
            "qs":qs
        }
        return render(request, self.template_name,self.args)

    def post(self, request, *args, **kwargs):
        id = kwargs.get("id")
        qs = FAQModel.objects.get(id=id)
        form = FAQModelForm(request.POST, instance=qs)
        if form.is_valid():
            form.save()
            messages.success(request, "FAQ Updated Successfully!!")
        else:
            messages.error(request, "FAQ unable to update!!")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


class FAQDeleteView(LoginRequiredMixin, View):
     def post(self, request, *args, **kwargs):
        id = kwargs.get("id")
        FAQModel.objects.get(id=id).delete()
        messages.success(request, "FAQ Deleted Successfully!!")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


class ServiceView(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = "services_admin.html"
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        tag_name = kwargs.get("servicetag")
        service_qs = ServiceModel.objects.filter(tag_name=tag_name).first()
        form = ServiceModelForm(instance=service_qs)
        self.args={
            "heading": service_qs.service_name,
            "service":service_qs,
            "form":form
            # "form":FAQModelForm()
        }
        return render(request,  self.template_name ,self.args)

    
    def post(self, request, *args, **kwargs):
        tag_name = kwargs.get("servicetag")
        service_qs = ServiceModel.objects.filter(tag_name=tag_name).first()
        service_img1 = request.FILES.get("service_img1","")
        service_img2 = request.FILES.get("service_img2","")
        service_img3 = request.FILES.get("service_img3","")
        form = ServiceModelForm(request.POST, request.FILES, instance=service_qs)
        if form.is_valid():
            a = form.save(commit=False)
            if service_img1 != "":
                a.main_service_image = service_img1
            if service_img2 != "":
                a.second_service_image = service_img2
            if service_img3 != "":
                a.third_service_image = service_img3
            a.save()
            messages.success(request, "Service Udated Successfully!!")
        else:
            messages.error(request, "Unable to update Service!!")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


class QuotesView(View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = "quotes.html"
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        quotes_qs = GetQuote.objects.all().order_by("-created_date")
        self.args={
            "heading": "Quotes Lists",
            "quotes":quotes_qs,
            # "form":FAQModelForm()
        }
        return render(request,  self.template_name ,self.args)


class QuotesDetailView(View):

    def dispatch(self, request, *args, **kwargs):
        self.template_name = "quotes_view.html"
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        quote_qs = GetQuote.objects.get(id=id)
        self.args={
            "heading": "Quotes",
            "quote_qs":quote_qs,
            # "form":FAQModelForm()
        }
        return render(request,  self.template_name ,self.args)


class PackageView(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = "package.html"
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        qs = PackageModel.objects.all().order_by("id")
        self.args={
            "heading": "Packages",
            "all_package":qs,
            # "form":FAQModelForm()
        }
        return render(request,  self.template_name ,self.args)

    def post(self, request, *args, **kwargs):
        form = FAQModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "FQA Added Successfully!!")
        else:
            messages.error(request, "Unable to add FQA!!")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


from django.db import transaction
class PackageAddView(View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = "package_add.html"
        self.args = {}
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        # qs = PackageModel.objects.all().order_by("id")
        self.args={
            "heading": "Add Packages",
            "shipper_modla":ShipperModelForm(),
            "receiver_modal":ReceiverModelForm(),
            "package_form":PackageModelForm(),
            # "all_package":qs,
            # "form":FAQModelForm()
        }
        return render(request,  self.template_name ,self.args)

    def post(self, request):
        shipper_form = ShipperModelForm(request.POST)
        receiver_form = ReceiverModelForm(request.POST)
        package_form = PackageModelForm(request.POST)
        all_info = self.request.POST.dict()
        i=0
        package_details = []
        for index in range(i,len(all_info)):
            flag=0
            if 'group-a['+str(index)+ "][package_name]" in request.POST:
                
                package_name = all_info[f"group-a[{index}][package_name]"]
                flag=1
            
            if 'group-a['+str(index)+ "][package_weight]" in request.POST:
                
                package_weight = all_info[f"group-a[{index}][package_weight]"]
                flag=1

            if 'group-a['+str(index)+ "][package_quantity]" in request.POST:
                
                package_quantity = all_info[f"group-a[{index}][package_quantity]"]
                flag=1


            if 'group-a['+str(index)+ "][package_rate]" in request.POST:
                
                package_rate = all_info[f"group-a[{index}][package_rate]"]
                flag=1

            if 'group-a['+str(index)+ "][package_total]" in request.POST:
                
                package_total = all_info[f"group-a[{index}][package_total]"]
                flag=1

            if flag == 1: 
                package_info = PackageDetailsModel.objects.create(package_name=package_name,total_weight=package_weight, total_quantity=package_quantity,rate=package_rate,grand_total= package_total  )
                package_details.append(package_info.id)

        print(package_details)
        if shipper_form.is_valid() and receiver_form.is_valid() and package_form.is_valid():
            shipper_ins = shipper_form.save()
            receiver_ins = receiver_form.save()
            m = package_form.save(commit=False)
            m.shipper = shipper_ins
            m.receiver = receiver_ins
            m.save()
            m.package_details.add(*PackageDetailsModel.objects.filter(id__in=package_details))
            m.save()
            TrackingModel.objects.create(package=m)

        # PackageModel.objects.create(shipper=shipper_ins,receiver=receiver_ins,package_details=package_info  )

        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

from django.http import JsonResponse
class TrackingStatsChangeView(View):
    def post(self ,request, *args, **kwargs):
        tracking_id = request.POST.get("track_id")
        status = request.POST.get("status")
        stats = TrackingStatus.objects.filter(name=status).first()
        a = TrackingModel.objects.filter(id=tracking_id).update(status=stats)
        return JsonResponse({"success":True})




class PackageEditView(LoginRequiredMixin, View):

    def dispatch(self, request, *args, **kwargs):
        self.template_name = "faq_edit.html"
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        qs = FAQModel.objects.get(id=id)
        self.args={
            "heading": "Edit FAQ",
            "form": FAQModelForm(instance=qs),
            "qs":qs
        }
        return render(request, self.template_name,self.args)

    def post(self, request, *args, **kwargs):
        print(2222222222222222)
        print(self.request.POST.dict())
        # id = kwargs.get("id")
        # qs = FAQModel.objects.get(id=id)
        # form = FAQModelForm(request.POST, instance=qs)
        # if form.is_valid():
        #     form.save()
        #     messages.success(request, "FAQ Updated Successfully!!")
        # else:
        #     messages.error(request, "FAQ unable to update!!")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


class PackageDeleteView(LoginRequiredMixin, View):
     def post(self, request, *args, **kwargs):
        id = kwargs.get("id")
        FAQModel.objects.get(id=id).delete()
        messages.success(request, "FAQ Deleted Successfully!!")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


class TrackingView(LoginRequiredMixin, View):

    def dispatch(self, request, *args, **kwargs):
        self.template_name = "tracking_admin.html"
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        all_package_tracking = TrackingModel.objects.all()[::-1]
        all_status =  TrackingStatus.objects.all()
        self.args = {
            "all_status":all_status,
            "tracking":all_package_tracking
        }
        return render(request, self.template_name,self.args)


class TrackingEditView(View, LoginRequiredMixin):

    def dispatch(self, request, *args, **kwargs):
        self.template_name = "tracking_edit.html"
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request, *args, **kwargs):
        id = kwargs.get("id")
        qs = TrackingModel.objects.get(id=id)
        self.args={
            "heading": "Edit Tracking Information",
            "form": TrackingModelForm(instance=qs),
            "qs":qs
        }
        return render(request, self.template_name,self.args)

    def post(self, request, *args, **kwargs):
        id = kwargs.get("id")
        qs = TrackingModel.objects.get(id=id)
        form = TrackingModelForm(request.POST, instance=qs)
        if form.is_valid():
            form.save()
            messages.success(request, "Tracking Stats Updated Successfully!!")
        else:
            messages.error(request, "Tracking unable to update!!")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


class TrackingDeleteView(LoginRequiredMixin, View):
     def post(self, request, *args, **kwargs):
        id = kwargs.get("id")
        TrackingModel.objects.get(id=id).delete()
        messages.success(request, "Tracking Deleted Successfully!!")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

class ShowStatusView(LoginRequiredMixin, View):

    def dispatch(self, request, *args, **kwargs):
        self.template_name = "tracking.html"
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        qs = FAQModel.objects.get(id=id)
        self.args={
            "heading": "Edit FAQ",
            "form": FAQModelForm(instance=qs),
            "qs":qs
        }
        return render(request, self.template_name,self.args)

    def post(self, request, *args, **kwargs):
        tracking_code = kwargs.get("id")
        FAQModel.objects.get(id=id).delete()
        messages.success(request, "FAQ Deleted Successfully!!")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
