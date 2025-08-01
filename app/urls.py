from django.urls import path
from .views import home,contactus,blogs,gallery
urlpatterns = [
   path("",home,name="home_page"),
   path("contact/",contactus,name="contact"),
   path("blogs/",blogs,name="blogs"),
   path("gallery/",gallery,name="gallery")
]