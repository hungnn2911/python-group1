from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from .models import MyUser, Room, Jobsummary


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

        if request.FILES["upload_file"]:
            myfile = request.FILES['upload_file']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
       
    
        newjobsummary = Jobsummary(
            room_id= roomid,
            type_summary= type_summary,
            description= description,
            document = document,
            deadline_plan = deadline_plan,
            deadline= deadline,
            upload_file=filename or None
        )
        newjobsummary.save()

        return redirect ("Danh_sach_KLGB")
    
def editjobsummary(request, pk):
    jobsummary = get_object_or_404(Jobsummary, pk=pk)
    rooms = Room.objects.all()
    type_summary = Jobsummary.SUMMARY_TYPES

    if request.method == "POST":
        data = request.POST
        jobsummary.room_id = int(data.get("room", ""))           
        jobsummary.type_summary = data.get("type_summary", "")
        jobsummary.description= data.get("description", "")
        jobsummary.document = data.get("document", "")
        jobsummary.deadline_plan= data.get("deadline_plan", "")
        jobsummary.deadline= data.get ("deadline", "")

        jobsummary.save()

        return redirect ("Danh_sach_KLGB")        

    return render(request, "job_summary/editjobsummary.html", context={"jobsummary": jobsummary, "rooms": rooms, "type_summaries": type_summary})

def detelejobsummary(request, pk):
    jobsummary = get_object_or_404(Jobsummary, pk=pk)
    jobsummary.delete()

    return redirect ("Danh_sach_KLGB")

def listjobsummary(request):
    listjobsummary = Jobsummary.objects.all()
    return render(request, "job_summary/listjobsummary.html",{"showjobsummary": listjobsummary})

# def uploadfile(request):
#     if request.method == 'POST' and request.FILES['myfile']:
#         myfile = request.FILES['myfile']
#         fs = FileSystemStorage()
#         filename = fs.save(myfile.name, myfile)
#         uploaded_file_url = fs.url(filename)
#         return render(request, 'uploads/upload.html', {
#             'uploaded_file_url': uploaded_file_url
#         })
#     return render(request, 'uploads/upload.html')


    

def KLGBinvestment(request, method="GET"):
    summary1 = Jobsummary.objects.filter(type_summary[2][0])
    return render(request, "job_summary/KLGBinvestment.html", {"jobsummary":summary1})

def KLGBmeeting(request, method="GET"):
    summary2 = Jobsummary.objects.filter(type_summary[0][0])
    return render(request, "job_summary/KLGBmeeting.html", {"jobsummary": summary2})

def KLGBoperation(request, method="GET"):
    summary3 = Jobsummary.objects.filter(type_summary[1][0])
    return render(request, "job_summary/KLGBoperation.html", {"jobsummary": summary3})

def KLGBother(request, method="GET"):
    summary4 = Jobsummary.objects.filter(type_summary[3][0])
    return render(request, "job_summary/KLGBother.html", {"jobsummary": summary4})


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




def Editroom(request, pk):
    room = get_object_or_404(Room, pk=pk)
    
    if request.method == "POST":
        data= request.POST
        room.name= data.get("name", "")
        room.code= data.get("code", "")
        room.save()

        return redirect("List_room")

    return render(request, "rooms/edit_room.html", context={"room": room})

def Edituser(request, pk):
    user = get_object_or_404(MyUser, pk=pk)
    rooms = Room.objects.all()
    roles= MyUser.ROLES

    if request.method == "POST":
        data = request.POST
       
        user.name= data.get("fullname", "")
        user.position= data.get("position", "")
        user.roomid= data.get("room", "")
        user.email= data.get("user_email", "")
        user.password= data.get("user_password", "")
        user.role= data.get("role", "")
        
        user.save()
        return redirect("List_user")

    return render(request, "users/edit_user.html", context={"user": user, "list_rooms": rooms, "list_role": roles})

def Deleteroom(request,pk):
    room = get_object_or_404(Room, pk=pk)
    # if request.method == "GET"
    # users = room.myuser_set.all()

    room.delete()

    return redirect("List_room")

def Deleteuser(request,pk):
    user = get_object_or_404(MyUser, pk=pk)

    user.delete()
    return redirect("List_user")     
