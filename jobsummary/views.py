from django.shortcuts import render, HttpResponseRedirect, redirect 
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

<<<<<<< HEAD
from .models import Jobsummary 
from .models import MyUser, Room

def createjobsummary(request):
    if request.method == "GET":
        return render (request, "job_summary/createjobsummary.html")

    elif request.method == "POST":
        data = request.POST
        name = data.get("room", " ")


=======
from .models import Jobsummary, Room
>>>>>>> create_dat/list



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

def createjobsummary(request):
    if request.method == "GET":
        rooms = Room.objects.all()
        type_summary = Jobsummary.SUMMARY_TYPES
        
        return render(request, "job_summary/createjobsummary.html", {"rooms":rooms, "type_summaries": type_summary})   
    elif request.method == "POST":
        data = request.POST    
        roomid= data.get("room", "")           
        type_summary = data.get("type_summary", "")
        description= data.get("description", "")
        document = data.get("document", "")
        deadline_plan= data.get("deadline_plan", "")
        deadline= data.get ("deadline", "")
       
    
    newjobsummary(
        room_id= roomid,
        type_summary= type_summary,
        description= description,
        document = document,
        deadline_plan = deadline_plan,
        deadline= deadline
    )
    type_summary.save()
    return redirect ("listjobsummary")
    

def KLGBinvestment(request, method="GET"):
    summary1 = Jobsummary.objects.all()
    return render(request, "job_summary/KLGBinvestment.html", {"jobsummary":summary1})

def KLGBmeeting(request, method="GET"):
    summary2 = Jobsummary.objects.all()
    return render(request, "job_summary/KLGBmeeting.html", {"jobsummary": summary2})

def KLGBoperation(request, method="GET"):
    summary3 = Jobsummary.objects.all()
    return render(request, "job_summary/KLGBoperation.html", {"jobsummary": summary3})

def KLGBother(request, method="GET"):
    summary4 = Jobsummary.objects.all()
    return render(request, "job_summary/KLGBother.html", {"jobsummary": summary4})

<<<<<<< HEAD

def Createuser(request):
    if request.method =="GET":
        rooms = Room.objects.all()
        roles= MyUser.ROLES
        return render (request, "users/create_user.html", {"list_rooms": rooms, "list_role": roles})

    elif request.method=="POST":
        data= request.POST
        name= data.get("fullname", "")
        position= data.get("position", "")
        roomid= data.get("room", "")
        email= data.get("email", "")
        password= data.get("password", "")
        role= data.get("role", "")

        newuser= MyUser(
            fullname= name,
            position= position,
            room_id= roomid,
            email= email,
            password= password,
            role= role)

        newuser.save()
    
    return redirect("List_user")

def Listuser(request, method="GET"):
    listuser= MyUser.objects.all()
    return render(request, "users/list_user.html", {"showuser": listuser})


def Create_room(request):
    if request.method=="GET":
        return render(request, "rooms/create_room.html")
    elif request.method=="POST":
        data= request.POST
        name= data.get("name", "")
        code= data.get("code", "")

        newroom= Room(
            name= name,
            code= code
        )

        newroom.save()
    return redirect("List_room")
    

def Listroom(request, method="GET"):
    listroom= Room.objects.all()
    return render(request, "rooms/list_room.html", {"showroom": listroom})
=======
def listjobsummary(request):
    return render(request, "job_summary/listjobsummary.html")

>>>>>>> create_dat/list
