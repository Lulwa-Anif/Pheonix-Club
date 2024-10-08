from django.shortcuts import render
from .models import Contact




def ContactUsView(request):
    if request.method=="POST":
        name = request.POST.get("name","")
        email = request.POST.get("email","")
        subject = request.POST.get("subject","")
        message= request.POST.get("message","")

        Contact.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message,
            )
        return render(request, "contact_us.html")
    return render(request, "contact_us.html")

def Home(request):
    return render(request,"home.html")

def About(request):
    return render(request,"About.html")

def Events(request):
    return render(request,"events.html")

def Gallery(request):
    return render(request,"gallery.html")