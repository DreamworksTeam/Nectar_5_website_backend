from django import forms
from .models import Support, Contact_us, Get_started
from django.utils.translation import gettext_lazy as _



# Support Form
class Support_Form(forms.ModelForm):
    class Meta:
        model = Support
        fields = ['full_name', 'phone', 'email', 'problem', 'complaint']
        labels = {
            'full_name': '',
            'phone': '',
            'email': '',
            'problem': 'Problem',
            'complaint': '',

        }
        widgets = {
            'full_name': forms.TextInput(attrs = {'placeholder': 'Enter Full Name:'}),
            'phone': forms.TextInput(attrs= {'placeholder': 'Enter Phone'}),
            'email': forms.TextInput(attrs={'placeholder': 'Enter Email'}),
            'complaint': forms.Textarea(attrs={'placeholder': 'Enter Complaint'})

            
        }

# contact us form
class Contact_Form(forms.ModelForm):
    class Meta:
        model = Contact_us
        fields = ['full_name', 'email', 'subject', 'message']
        labels = {
            'full_name': '',
            'email': '',
            'subject': '',
            'message': '',
        }
        widgets  = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Enter Full Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Enter Email'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Enter Subject'}),
            'message': forms.Textarea(attrs={'placeholder': 'Enter Message'}),

        }

# get started form
class Get_Started_Form(forms.ModelForm):
    class Meta:
        model = Get_started
        fields = ['organization', 'email', 'phone', 'location', 'entry']
        labels = {
            'organization': '',
            'email': '',
            'phone': '',
            'location': 'Location',
            'entry': '',
        }
        widgets = {
            'organization': forms.TextInput(attrs={'placeholder': 'Enter Organization'}),
            'email': forms.TextInput(attrs={'placeholder': 'Enter Email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Enter Phone Number'}),
            'entry': forms.Textarea(attrs={'placeholder': 'Data Collection Enquiry'}),
        }