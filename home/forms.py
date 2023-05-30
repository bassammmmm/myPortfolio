from django import forms
from .models import ContactMessage
class ContactMesssageForm(forms.ModelForm):
    
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Your Name'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Your Email'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder' : 'Message', 'rows' : '5'}))
    
    class Meta:
        model = ContactMessage
        fields = '__all__'