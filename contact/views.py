from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import ContactForm

# Create your views here.
def contact(request):
    if request.method=="POST":
       form = ContactForm(request.POST)
       if form.is_valid():
           #form.save()
           return HttpResponse('Success! Thank you for the message, Will get back to you shortly')
    else:
        form=ContactForm()
        return render(request,'contact.html',{'form':form})


#def contact(request):
 #   return render(request,'contact.html',{})