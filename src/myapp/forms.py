from django.forms import ModelForm
from django import forms
from myapp.models import Feedback


class ContactForm(forms.Form):
    from_email=forms.EmailField(required=True)
    subject=forms.CharField(required=True)
    message=forms.CharField(widget=forms.Textarea,required=True)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model=Feedback
        fields="__all__"
