from django.contrib import admin

from .models import *

class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ["site_name","mode"]

admin.site.register(SiteSetting, SiteSettingAdmin)

admin.site.register(SystemSettings)

admin.site.register(Profile)
admin.site.register(Ecommerce)
admin.site.register(CheckoutInquiry)

class OverviewBannerModelAdmin(admin.ModelAdmin):
    list_display = ["text1"]

admin.site.register(OverviewBannerModel, OverviewBannerModelAdmin)


class ContactUsModelAdmin(admin.ModelAdmin):
    list_display = ["name","email","phone","subject"]

admin.site.register(ContactUsModel, ContactUsModelAdmin)


class BlogModelAdmin(admin.ModelAdmin):
    list_display = ["title","created_by"]

    def created_by(self, instance):
        try:return instance.created_by.username
        except AttributeError as e: return None

admin.site.register(BlogModel, BlogModelAdmin)

class CommentModelAdmin(admin.ModelAdmin):
    list_display = ["blog","title","creater_name","creater_email"]

admin.site.register(CommentModel, CommentModelAdmin)
admin.site.register(Teams)

admin.site.register(FAQModel)

class TestimonialsModelAdmin(admin.ModelAdmin):
    list_display = ["user_name","designation"]

admin.site.register(TestimonialsModel, TestimonialsModelAdmin)

class AboutUsModelAdmin(admin.ModelAdmin):
    list_display = ["main_text","delivery_packages","countries_covered","happy_clients","tons_of_good"]

admin.site.register(AboutUsModel, AboutUsModelAdmin)

class ServiceModelAdmin(admin.ModelAdmin):
    list_display = ["tag_name","service_name"]

admin.site.register(ServiceModel, ServiceModelAdmin)
admin.site.register(GetQuote)
admin.site.register(CourierModel)
admin.site.register(CargoModelPackage)
admin.site.register(DeliveryMode)
admin.site.register(ShipperModel)
admin.site.register(ReceiverModel)
admin.site.register(PackageDetailsModel)
admin.site.register(PackageModel)
admin.site.register(TrackingStatus)
admin.site.register(TrackingModel)


