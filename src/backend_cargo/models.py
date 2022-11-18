from email.policy import default
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

class Teams(models.Model):
    full_name = models.CharField(max_length=100)
    user_image =  models.FileField(upload_to="teams_pic", 
        validators=[FileExtensionValidator(allowed_extensions=settings.VALID_IMAGE_FORMAT)], null=True)
    designation = models.CharField(max_length=50, null=False, blank=False)
    fb_url = models.URLField(max_length=100 , null=True, blank=True)
    insta_url = models.URLField(max_length=100, null=True, blank=True)
    twitter_url = models.URLField(max_length=100, null=True, blank=True)
    linkedin_url = models.URLField(max_length=100, null=True, blank=True)
    tiktok_url = models.URLField(max_length=100, null=True, blank=True)


    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = ("Teams Setting")
        verbose_name_plural = ("Teams Setting")


class SiteSetting(AuditFields):
    CHOICES = (
        ('Live', 'Live'),
        ('Down', 'Down'),
        ('Maintainance', 'Maintainance'),
    )
    site_name=models.CharField(max_length=30)
    logo_image = models.FileField(upload_to="logo", 
        validators=[FileExtensionValidator(allowed_extensions=settings.VALID_IMAGE_FORMAT)], null=True)
    mode=models.CharField(max_length=20, choices=CHOICES, default='Live')
    description = models.TextField(null=True, blank=True)
    favicon =  models.FileField(upload_to="logo", 
        validators=[FileExtensionValidator(allowed_extensions=settings.VALID_IMAGE_FORMAT)], null=True)
    

    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name = ("Site Setting")
        verbose_name_plural = ("Site Setting")

    @property
    def sitename(self):
        return self.site_name

class SystemSettings(AuditFields):
    contact_email=models.EmailField()
    phone_number= models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    fb_url = models.URLField(max_length=100 , null=True, blank=True)
    insta_url = models.URLField(max_length=100, null=True, blank=True)
    twitter_url = models.URLField(max_length=100, null=True, blank=True)
    linkedin_url = models.URLField(max_length=100, null=True, blank=True)
    tiktok_url = models.URLField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.contact_email

    class Meta:
        verbose_name = ("System Setting")
        verbose_name_plural = ("System Setting")


class OverviewBannerModel(AuditFields):
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
    blog_image = models.FileField(upload_to="blog_image", 
        validators=[FileExtensionValidator(allowed_extensions=settings.VALID_IMAGE_FORMAT)], null=True)
    created_by = models.ForeignKey(User, verbose_name=("Created By"), on_delete=models.CASCADE)
    sub_image1 = models.FileField(upload_to="blog_image", 
        validators=[FileExtensionValidator(allowed_extensions=settings.VALID_IMAGE_FORMAT)], null=True)

    sub_image2 = models.FileField(upload_to="blog_image", 
        validators=[FileExtensionValidator(allowed_extensions=settings.VALID_IMAGE_FORMAT)], null=True)
    highlighted_text = models.CharField(max_length=255, null=True, blank=True)
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
    description = models.TextField(null=False, blank=False)
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
    service_name =  models.CharField(max_length=150, null=False, blank=False)
    main_service_image =  models.FileField(upload_to="service", 
        validators=[FileExtensionValidator(allowed_extensions=settings.VALID_IMAGE_FORMAT)], null=True)
    first_text =  models.CharField(max_length=150, null=False, blank=False)
    first_description = models.TextField(null=False, blank=False)
    second_text =  models.CharField(max_length=150, null=False, blank=False)
    second_description = models.TextField(null=False, blank=False)
    second_service_image =  models.FileField(upload_to="service", 
        validators=[FileExtensionValidator(allowed_extensions=settings.VALID_IMAGE_FORMAT)], null=True)
    third_text =  models.CharField(max_length=150, null=False, blank=False)
    third_description = models.TextField(null=False, blank=False)
    third_service_image =  models.FileField(upload_to="service", 
            validators=[FileExtensionValidator(allowed_extensions=settings.VALID_IMAGE_FORMAT)], null=True)
    def __str__(self):
        return self.tag_name

    class Meta:
        verbose_name = ("Service")
        verbose_name_plural = ("Services")

class CourierModel(models.Model):
    courier_type = models.CharField(max_length=50)

    def __str__(self):
        return self.courier_type

class CargoModelPackage(models.Model):
    cargo_type = models.CharField(max_length=50, null=True, blank=False)
    test = models.BooleanField((""))

    def __str__(self):
        return self.cargo_type


class DeliveryMode(models.Model):
    mode = models.CharField(max_length=50)

    def __str__(self):
        return self.mode

class ShipperModel(AuditFields):
    name = models.CharField(max_length=50, null=True, blank=False)
    hotel = models.CharField(max_length=150, null=True, blank=False)
    room_no = models.IntegerField()
    passpord_number = models.CharField(max_length=50, null=True, blank=False)
    nationality = models.CharField(max_length=50, null=True, blank=False)

    def __str__(self):
        return self.name

class ReceiverModel(AuditFields):
    name = models.CharField(max_length=50, null=True, blank=False)
    address = models.CharField(max_length=150, null=True, blank=False)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=50, null=True, blank=False)
    airport = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=150, null=True, blank=True)
    phone = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.name



class GetQuote(AuditFields):

    freight_type = (
        ("Express Delivery", "Express Delivery"),
        ("Ocean Freight", "Ocean Freight"),
        ("Road Freight", "Road Freight"),
        ("Air Freight", "Air Freight")
    ) 

    full_name = models.CharField(max_length=100,null=True, blank=True)
    email = models.EmailField(max_length=254,null=True, blank=True)
    phone = models.CharField(max_length=50,null=True, blank=True)
    flight_type = models.ForeignKey(CourierModel, verbose_name=("Type of Carrier"), on_delete=models.CASCADE)
    city_departure = models.CharField(max_length=50,null=True, blank=True)
    city = models.CharField(max_length=50,null=True, blank=True)
    width = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    length = models.FloatField(null=True, blank=True)
    type_freight = models.CharField(max_length=50, choices=freight_type, null=True, blank=True)

    class Meta:
        verbose_name = ("GetQuote")
        verbose_name_plural = ("GetQuotes")

    def __str__(self):
        return self.full_name



class PackageDetailsModel(AuditFields):
    package_name =  models.CharField(max_length=150, null=True, blank=True)
    total_weight = models.FloatField()
    total_quantity = models.IntegerField()
    rate = models.FloatField()
    grand_total = models.FloatField(null=True)

    def __str__(self):
        return self.package_name



class PackageModel(AuditFields):
    CHOICES = (
        ('Esewa', 'Esewa'),
        ('Khalti', 'Khalti'),
        ('Bank Transfer', 'Bank Transfer'),
        ('Cash', 'Cash'),
        ('Other', 'Other')
    )
    shipper = models.ForeignKey(ShipperModel, verbose_name=("Shipper Details"), on_delete=models.CASCADE)
    receiver = models.ForeignKey(ReceiverModel, verbose_name=("Receiver Details"), on_delete=models.CASCADE)
    package_details = models.ManyToManyField(PackageDetailsModel, verbose_name=("Related Packages"))
    courier = models.ForeignKey(CourierModel, verbose_name=("Courier"), on_delete=models.CASCADE, null=True, blank=True)
    cargo = models.ForeignKey(CargoModelPackage, verbose_name=("Cargo Details"), on_delete=models.CASCADE, null=True, blank=True)
    mode = models.ForeignKey(DeliveryMode, verbose_name=("Delivery Mode"), on_delete=models.CASCADE)
    expected_delivery_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    payment_mode = models.CharField(max_length=20, choices=CHOICES, default='Cash')
    is_picked_up = models.BooleanField(default=False)
    comments = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.shipper.name


class TrackingStatus(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

class TrackingModel(AuditFields):

    tracking_code = models.PositiveIntegerField(("Tracking Code"), null=True, blank=True)
    package = models.ForeignKey(PackageModel, verbose_name=("Package Details"),related_name="package_details_cargo", on_delete=models.CASCADE, null=True, blank=True)
    status = models.ForeignKey(TrackingStatus, verbose_name=("Tracking Status"), on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True,blank=True)
    location = models.CharField(max_length=250,null=True,blank=True)
    class Meta:
        verbose_name = ("Tracking Model")
        verbose_name_plural = ("Tracking Models")

    def __str__(self) -> str: 
        return str(self.tracking_code)

    def save(self, *args, **kwargs):
        if self.tracking_code == None:
            code=''.join(random.choice('0123456789') for i in range(9))
        
            self.tracking_code = code
        return super().save(*args, **kwargs)

