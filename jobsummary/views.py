from django.shortcuts import render, HttpResponseRedirect 
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Jobsummary

# Create your views here.
def user_login(request, method="POST"):
    if request.method == "POST":
        email = request.POST.get("email", "")
        password = request.POST.get("password","")
        user = authenticate(email=email, password=password)

        if user is None:
            my_message= (
                "Your email address or password is incorrect. Please login again"
            )
            messages.error(request, my_message)
            return render(request, "layouts/login.html")

        login(request, user)
        return HttpResponseRedirect("dashboard/")

    return render(request, "layouts/login.html")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/")  

@login_required
def dashboard(request):
    return render(request, "dashboard/statistic.html")

def KLGBmeeting(request):
    return render(request, "job_summary/KLGBmeeting.html")
    
def KLGBoperation(request):
    return render(request, "job_summary/KLGBoperation.html")    

def KLGBinvestment(request):
    jobs = Jobsummary.objects.all
    return render(request, "job_summary/KLGBinvestment.html", {"jobsumary": jobs})

def KLGBother(request):
    return render(request, "job_summary/KLGBother.html")

def createjobsummary(request):
    return render(request, "job_summary/createjobsummary.html")
