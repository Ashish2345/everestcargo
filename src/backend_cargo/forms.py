from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column

from allauth.account.forms import LoginForm

from django import forms

from .models import (OverviewBannerModel, AboutUsModel, SiteSetting, SystemSettings, Teams,
                    BlogModel, TestimonialsModel, FAQModel, ServiceModel,ShipperModel,
                    ReceiverModel,PackageModel, TrackingModel )


class UserLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.fields['login'].widget = forms.TextInput(attrs={'class': 'form-control mb-2','placeholder':'Enter Username','id':'username'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2','placeholder':'Enter Password','id':'password'})
        self.fields['remember'].widget = forms.CheckboxInput(attrs={'class': 'form-check-input'})


class OverviewBannerModelForm(forms.ModelForm):

        text1 = forms.CharField(
            label = "Banner Text 1",
            required=True)

        text2 = forms.CharField(
            label = "Banner Text 2",
            required=True)

        text3 = forms.CharField(
            label = "Banner Text 3",
            required=True)

        def __init__(self,*args,**kwargs):

            super ().__init__(*args,**kwargs) 
        
            self.helper = FormHelper()
            self.helper.form_tag = False
            self.helper.layout = Layout(
            Row(
                Column('text1', css_class='form-group col-md-12 mb-3'),
                css_class='form-row'
            ),
            Row(
                Column('text2', css_class='form-group col-md-12 mb-3'),
                css_class='form-row'
            ),
            Row(
                Column('text3', css_class='form-group col-md-12 mb-3'),
                css_class='form-row'
            ),
            )

        class Meta:
            model = OverviewBannerModel
            fields = ("text1","text2", "text3")



class AboutModelForm(forms.ModelForm):

        main_text = forms.CharField(
            label = "About Text",
            required=True)


        def __init__(self,*args,**kwargs):

            super ().__init__(*args,**kwargs) 
        
            self.helper = FormHelper()
            self.helper.form_tag = False
            self.helper.layout = Layout(
            Row(
                Column('main_text', css_class='form-group col-md-12 mb-3'),
                css_class='form-row'
            ),
            Row(
                Column('delivery_packages', css_class='form-group col-md-12 mb-3'),
                css_class='form-row'
            ),
            Row(
                Column('countries_covered', css_class='form-group col-md-12 mb-3'),
                css_class='form-row'
            ),
            Row(
                Column('happy_clients', css_class='form-group col-md-12 mb-3'),
                css_class='form-row'
            ),
            Row(
                Column('tons_of_good', css_class='form-group col-md-12 mb-3'),
                css_class='form-row'
            ),
            Row(
                Column('description', css_class='form-group col-md-12 mb-3'),
                css_class='form-row'
            )
            )
            

        class Meta:
            model = AboutUsModel
            fields = ("main_text","description", "delivery_packages","countries_covered","happy_clients","tons_of_good")



class SiteOptionUpdateForm(forms.ModelForm):

    CHOICES = (
        ('Live', 'Live'),
        ('Down', 'Down'),
        ('Maintainance', 'Maintainance'),
    )
    mode=forms.ChoiceField(required=False, choices=CHOICES)

    class Meta:
        model=SiteSetting
        fields=['site_name','mode', 'description']


class SystemSettingsUpdateForm(forms.ModelForm):


    def __init__(self,*args,**kwargs):

            super ().__init__(*args,**kwargs) 
        
            self.helper = FormHelper()
            self.helper.form_tag = False
            self.helper.layout = Layout(
            Row(
                
                Column('contact_email', css_class='form-group col-lg-6 col-sm-0 mb-3'),
                Column('phone_number', css_class='form-group col-lg-6 col-sm-0 mb-3'),
                css_class='row'
            ),
            
            'address','fb_url', 'insta_url','twitter_url', 'linkedin_url', 'tiktok_url'
            )
    class Meta:
        model=SystemSettings
        fields=['contact_email','phone_number', 'address', 'fb_url', 'insta_url','twitter_url', 'linkedin_url', 'tiktok_url']


class TeamsForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):

            super ().__init__(*args,**kwargs) 
        
            self.helper = FormHelper()
            self.helper.form_tag = False
            self.helper.layout = Layout(
            Row(
                
                Column('full_name', css_class='form-group col-lg-6 col-sm-0 mb-3'),
                Column('designation', css_class='form-group col-lg-6 col-sm-0 mb-3'),
                css_class='row'
            ),
           Row(
                
                Column('fb_url', css_class='form-group col-lg-12 col-sm-0 mb-3'),
                css_class='row'
            ),
            Row(
                
                Column('insta_url', css_class='form-group col-lg-12 col-sm-0 mb-3'),
                css_class='row'
            ),
            Row(
                
                Column('twitter_url', css_class='form-group col-lg-12 col-sm-0 mb-3'),
                css_class='row'
            ),
            Row(
                
                Column('linkedin_url', css_class='form-group col-lg-12 col-sm-0 mb-3'),
                css_class='row'
            ),
            Row(
                
                Column('tiktok_url', css_class='form-group col-lg-12 col-sm-0 mb-3'),
                css_class='row'
            ),
            )
    class Meta:
        model=Teams
        fields=['full_name','user_image', 'designation', 'fb_url', 'insta_url','twitter_url', 'linkedin_url', 'tiktok_url' ]



class BlogForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):

            super ().__init__(*args,**kwargs) 
            self.helper = FormHelper()
            self.helper.layout = Layout(
           
            Row(
                
                Column('title', css_class='form-group col-lg-12 col-sm-0 mb-3'),
                css_class='row'
            ),
            
           
            Row(
                
                Column('highlighted_text', css_class='form-group col-lg-12 col-sm-0 mb-3'),
                css_class='row'
            ),
           Row(
                
                Column('description', css_class='form-group col-lg-12 col-sm-0 mb-4'),
                css_class='row'
            ),
            )
            
    class Meta:
        model=BlogModel
        fields=['title','description', 'highlighted_text']


class TestimonialsModelForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):

            super ().__init__(*args,**kwargs) 
            self.helper = FormHelper()
            self.helper.layout = Layout(
           
            Row(
                
                Column('user_name', css_class='form-group col-lg-12 col-sm-0 mb-3'),
                css_class='row'
            ),
            
           
            Row(
                
                Column('designation', css_class='form-group col-lg-12 col-sm-0 mb-3'),
                css_class='row'
            ),
           Row(
                
                Column('description', css_class='form-group col-lg-12 col-sm-0 mb-4'),
                css_class='row'
            ),
            )
            
    class Meta:
        model=TestimonialsModel
        fields=['user_name','designation', 'description']


class FAQModelForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):

            super ().__init__(*args,**kwargs) 
            self.helper = FormHelper()
            self.helper.layout = Layout(
           
            Row(
                
                Column('question', css_class='form-group col-lg-12 col-sm-0 mb-3'),
                css_class='row'
            ),
            
           
            Row(
                
                Column('answer', css_class='form-group col-lg-12 col-sm-0 mb-3'),
                css_class='row'
            ),
            )
    class Meta:
        model=FAQModel
        fields=['question','answer']


class ServiceModelForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):

            super ().__init__(*args,**kwargs) 
            self.helper = FormHelper()
            self.helper.layout = Layout(
           
            Row(
                
                Column('service_name', css_class='form-group col-lg-12 col-sm-0 mb-3'),
                css_class='row'
            ),
             Row(
                
                Column('first_text', css_class='form-group col-lg-12 col-sm-0 mb-3'),
                css_class='row'
            ),
             Row(
                
                Column('first_description', css_class='form-group col-lg-12 col-sm-0 mb-3'),
                css_class='row'
            ),
             Row(
                
                Column('second_text', css_class='form-group col-lg-12 col-sm-0 mb-3'),
                css_class='row'
            ),
             Row(
                
                Column('second_description', css_class='form-group col-lg-12 col-sm-0 mb-3'),
                css_class='row'
            ),
             Row(
                
                Column('third_text', css_class='form-group col-lg-12 col-sm-0 mb-3'),
                css_class='row'
            ),
             Row(
                
                Column('third_description', css_class='form-group col-lg-12 col-sm-0 mb-3'),
                css_class='row'
            ),
            
           
            
            )
    class Meta:
        model=ServiceModel
        fields=['service_name','first_text', "first_description","second_text","second_description","third_text","third_description" ]




class ShipperModelForm(forms.ModelForm):

        def __init__(self,*args,**kwargs):

            super ().__init__(*args,**kwargs) 
        
            self.helper = FormHelper()
            self.helper.form_tag = False
            self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-12 mb-3'),
               
            ),
            Row(
                Column('hotel', css_class='form-group col-md-12 mb-3'),
                
            ),
            Row(
                Column('room_no', css_class='form-group col-md-12 mb-3'),
                
            ),
        
             Row(
                Column('passpord_number', css_class='form-group col-md-12 mb-3'),
               
            ),
            Row(
                Column('nationality', css_class='form-group col-md-12 mb-3'),
                
            ),
            )

        class Meta:
            model = ShipperModel
            fields = ("name","hotel", "room_no","passpord_number","nationality")



class ReceiverModelForm(forms.ModelForm):

        def __init__(self,*args,**kwargs):

            super ().__init__(*args,**kwargs) 
        
            self.helper = FormHelper()
            self.helper.form_tag = False
            self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-12 mb-3'),
               
            ),
            Row(
                Column('address', css_class='form-group col-md-12 mb-3'),
                
            ),
            Row(
                Column('postal_code', css_class='form-group col-md-6 mb-3'),
                 Column('country', css_class='form-group col-md-6 mb-3'),
                 css_class='row'
            ),
        
           
            Row(
                Column('airport', css_class='form-group col-md-12 mb-3'),
                
            ),
            Row(
                Column('email', css_class='form-group col-md-6 mb-3'),
                Column('phone', css_class='form-group col-md-6 mb-3'),
                css_class='row'
            ),
            )

        class Meta:
            model = ReceiverModel
            fields = ("name","address", "postal_code","country","airport","email","phone")




class PackageModelForm(forms.ModelForm):

        expected_delivery_date = forms.DateField(
                widget=forms.TextInput(
                    attrs={'type': 'date'}
                )
            )

        def __init__(self,*args,**kwargs):

            super ().__init__(*args,**kwargs) 
        
            self.helper = FormHelper()
            self.helper.form_tag = False
            self.helper.layout = Layout(
            Row(
                Column('courier', css_class='form-group col-md-3 mb-3'),
                Column('cargo', css_class='form-group col-md-3 mb-3'),
                Column('mode', css_class='form-group col-md-3 mb-3'),
                Column('payment_mode', css_class='form-group col-md-3 mb-3'),
                css_class='row'
            ),

             
             Row(
                Column('expected_delivery_date', css_class='form-group col-md-12 mb-3'),
                
            ),
             Row(
                Column('comments', css_class='form-group col-md-12 mb-3'),
                
            ),
           
        
            )

        class Meta:
            model = PackageModel
            fields = ("courier","cargo", "mode","expected_delivery_date","payment_mode",'comments')






class TrackingModelForm(forms.ModelForm):

        def __init__(self,*args,**kwargs):

            super ().__init__(*args,**kwargs) 
        
            self.helper = FormHelper()
            self.helper.form_tag = False
            self.helper.layout = Layout(
            Row(
                Column('tracking_code', css_class='form-group col-md-12 mb-3'),
               
            ),
            Row(
                Column('package', css_class='form-group col-md-12 mb-3'),
                
            ),
             Row(
                Column('status', css_class='form-group col-md-12 mb-3'),
                
            ),
             Row(
                Column('description', css_class='form-group col-md-12 mb-3'),
                
            ),
           
        
           
            Row(
                Column('location', css_class='form-group col-md-12 mb-3'),
                
            ),

          
           
            )

        class Meta:
            model = TrackingModel
            fields = ("tracking_code","package", "status","description","location")