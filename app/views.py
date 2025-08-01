from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"index.html")

def contactus(request):
    return render(request,"contact.html")
def blogs(request):
    return render(request,"blogs.html")
def gallery(request):
    return render(request,"gallery.html")