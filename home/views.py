from django.shortcuts import render
#from .models import profile_pic
# Create your views here.
def home(request):
    #home=profile_pic.objects.all()
    #context={
     #   'home':home
    #}
    return render(request, 'home.html', {})