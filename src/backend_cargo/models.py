import random

from django.core.validators import FileExtensionValidator
from django.db import models
from django.conf import  settings
from django.urls import reverse

from django.contrib.auth.models import User


class AuditFields(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    updated_date = models.DateTimeField(auto_now=True,  null=True )

    class Meta:
        abstract = True


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    birthday = models.DateTimeField(auto_now_add=False,null=True,blank=True)
    gender = models.CharField(max_length=250, null=True,blank=True)
    address1 =  models.CharField(max_length=250, null=True,blank=True)
    phone = models.CharField(max_length=15, null=True,blank=True)
    profile_image =  models.FileField(upload_to="profile_pic", 
        validators=[FileExtensionValidator(allowed_extensions=settings.VALID_IMAGE_FORMAT)], null=True)


    def __str__(self):
        return self.user.username

class SiteSetting(models.Model):
    CHOICES = (
        ('Live', 'Live'),
        ('Down', 'Down'),
        ('Maintainance', 'Maintainance'),
    )
    site_name=models.CharField(max_length=30)
    logo_image = models.FileField(upload_to="logo", 
        validators=[FileExtensionValidator(allowed_extensions=settings.VALID_IMAGE_FORMAT)], null=True)
    contact_email=models.EmailField()
    mode=models.CharField(max_length=20, choices=CHOICES, default='Live')
    favicon =  models.FileField(upload_to="logo", 
        validators=[FileExtensionValidator(allowed_extensions=settings.VALID_IMAGE_FORMAT)], null=True)
    fb_url = models.URLField(max_length=100 , null=True, blank=True)
    insta_url = models.URLField(max_length=100, null=True, blank=True)
    twitter_url = models.URLField(max_length=100, null=True, blank=True)
    linkedin_url = models.URLField(max_length=100, null=True, blank=True)
    tiktok_url = models.URLField(max_length=100, null=True, blank=True)


    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name = ("Site Setting")
        verbose_name_plural = ("Site Setting")

    @property
    def sitename(self):
        return self.site_name


class OverviewBannerModel(models.Model):
    text1 = models.CharField(max_length=50, null=False, blank=False)
    text2 = models.CharField(max_length=100, null=False, blank=False)
    text3 = models.CharField(max_length=50, null=False, blank=False)
    banner_image = models.FileField(upload_to="banner", 
        validators=[FileExtensionValidator(allowed_extensions=settings.VALID_IMAGE_FORMAT)], null=True)

    class Meta:
        verbose_name = ("Banner Model")
        verbose_name_plural = ("Banner Models")


class ContactUsModel(AuditFields):
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=50, null=True, blank=True)
    subject = models.CharField(max_length=50, null=True, blank=True)
    message = models.TextField(null=False, blank=False)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = ("Contact Us")
        verbose_name_plural = ("Contact Us")


class BlogModel(AuditFields):
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    blog_image = models.FileField(upload_to="banner", 
        validators=[FileExtensionValidator(allowed_extensions=settings.VALID_IMAGE_FORMAT)], null=True)
    created_by = models.ForeignKey(User, verbose_name=("Created By"), on_delete=models.CASCADE)
    blog_image2 = models.FileField(upload_to="banner", 
        validators=[FileExtensionValidator(allowed_extensions=settings.VALID_IMAGE_FORMAT)], null=True)

    def __str__(self)-> str:
        return self.title

class CommentModel(AuditFields):
    blog = models.ForeignKey(BlogModel, verbose_name=("Blog Info"), on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=True, blank=True)
    creater_name = models.CharField(max_length=50, null=True, blank=True)
    creater_email = models.EmailField(max_length=50, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    def __str__(self)-> str:
        return self.title


class FAQModel(AuditFields):
    question = models.CharField(max_length=200, null=False, blank=False)
    answer = models.TextField(null=False, blank=False)

    def __str__(self)-> str:
        return self.question

    class Meta:
        verbose_name = ("FAQ Configuration")
        verbose_name_plural = ("FAQ Configurations")


class TestimonialsModel(AuditFields):

    user_image =  models.FileField(upload_to="user_img", 
        validators=[FileExtensionValidator(allowed_extensions=settings.VALID_IMAGE_FORMAT)], null=True)
    user_name = models.CharField(max_length=50, null=False, blank=False)
    designation = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=False, blank=False)


    def __str__(self)-> str:
        return self.user_name

    class Meta:
        verbose_name = ("Testimonial")
        verbose_name_plural = ("Testimonials")


class AboutUsModel(AuditFields):
    main_image =  models.FileField(upload_to="about_us", 
        validators=[FileExtensionValidator(allowed_extensions=settings.VALID_IMAGE_FORMAT)], null=True)
    main_text = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=50, null=False, blank=False)
    delivery_packages = models.IntegerField(null=False, blank=False)
    countries_covered = models.IntegerField(null=False, blank=False)
    happy_clients = models.IntegerField(null=False, blank=False)
    tons_of_good = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.main_text

    class Meta:
        verbose_name = ("About Us")
        verbose_name_plural = ("About Us")


class ServiceModel(AuditFields):
    tag_name = models.CharField(max_length=50, null=False, blank=False)
    service_name =  models.CharField(max_length=50, null=False, blank=False)
    main_service_image =  models.FileField(upload_to="service", 
        validators=[FileExtensionValidator(allowed_extensions=settings.VALID_IMAGE_FORMAT)], null=True)
    first_text =  models.CharField(max_length=100, null=False, blank=False)
    first_description = models.TextField(null=False, blank=False)
    second_text =  models.CharField(max_length=100, null=False, blank=False)
    second_description = models.TextField(null=False, blank=False)
    third_text =  models.CharField(max_length=100, null=False, blank=False)
    third_description = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.tag_name

    class Meta:
        verbose_name = ("Service")
        verbose_name_plural = ("Services")

# class Packageinformation(models.Model):
#     name_of_receipt = models.CharField(max_length=50)
#     hotel  = models.CharField(max_length=50)
#     name_of_receipt = models.CharField(max_length=50)
#     name_of_receipt = models.CharField(max_length=50)
#     name_of_receipt = models.CharField(max_length=50)

#     class Meta:
#         verbose_name = ("")
#         verbose_name_plural = ("s")

#     def __str__(self):
#         return self.name


class TrackingModel(models.Model):

    tracking_code = models.PositiveIntegerField(("Tracking Code"))



    class Meta:
        verbose_name = ("Tracking Model")
        verbose_name_plural = ("Tracking Models")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.tracking_code == None:
            code=''.join(random.choice('0123456789') for i in range(9))
            has_code = self.__class__.filter(tracking_code=code).exists()
            count = 1
            while has_code:
                count += 1
                has_code =self.__class__.objects.filter(tracking_code=code).exists()
            self.tracking_code = code

        return super().save(*args, **kwargs)

