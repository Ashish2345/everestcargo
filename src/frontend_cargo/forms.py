from django import forms
from backend_cargo.models import CheckoutInquiry

class CheckoutInquiryForm(forms.ModelForm):
    
    class Meta:
        model = CheckoutInquiry
        exclude = ("product","quantity")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                "class": "form-control"
            })
    