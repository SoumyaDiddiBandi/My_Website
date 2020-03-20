from django import forms
from .models import Post

class ContactForm(forms.Form):
    Your_Name=forms.CharField(label='Your Name', max_length=100)
    Your_Email=forms.CharField(label='Your Email', max_length=200)
    Message=forms.CharField(widget=forms.Textarea,required=True)
'''class Meta:
    model = Post
    fields = {'post',}
'''