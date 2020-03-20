from django.urls import path
from . import views
from .views import ContactForm

urlpatterns=[
    path("",views.contact,name="contact"),
   # path("",views.thanks,name="thanks")


]