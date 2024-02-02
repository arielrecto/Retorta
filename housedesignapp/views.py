from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from housedesignapp.models import *
from housedesignapp.forms import *
import json
from django.core.serializers import serialize

# Create your views here.


def home(request):
    return render(request, "pages/home.html")


def sign_in(request):
    if request.user.is_authenticated:
        return redirect(to="dashboard")

    if request.method == "POST":
        user = {
            "username": request.POST.get("username"),
            "password": request.POST.get("password"),
        }

        userAuth = authenticate(
            request, username=user["username"], password=user["password"]
        )

        if userAuth is not None:
            login(request, userAuth)
            return redirect(to="dashboard")

    return render(request, "pages/login.html")




def gallery(request):
    projects = Project.objects.all()
    
    projectJson = serialize('json', projects)
    

    context = {
        'projects' : projects,
        'projectJson' : projectJson
    }
    
    return render(request, "pages/gallery.html", context)



@login_required(login_url="login")
def sign_out(request):
    logout(request)
    return redirect(to="home")

@login_required(login_url="login")
def dashboard(request):
    appointments = Appointment.objects.all()
    inbox = Inbox.objects.all()
    projects = Project.objects.all()

    context = {
        "appointments": appointments,
        "total_appointments": appointments.count(),
        "inbox": inbox,
        "total_inbox": inbox.count(),
        "projects": projects,
        "total_projects": projects.count(),
    }

    return render(request, "pages/dashboard.html", context)


@login_required(login_url="login")
def project_list(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "pages/project/index.html", context)


@login_required(login_url="login")
def project_show(request, projectID):
    project = Project.objects.get(id=projectID)

    context = {"project": project}

    print(context)

    return render(request, "pages/project/show.html", context)


@login_required(login_url="login")
def project_create(request):
    if request.method == "POST":
        projectData = {
            "name": request.POST.get("name"),
            "price": request.POST.get("price"),
            "description": request.POST.get("description"),
            "image": request.FILES["project_image"],
        }

        project = Project.objects.create(
            name=projectData["name"],
            image=projectData["image"],
            price=projectData["price"],
            description=projectData["description"],
        )

        if project is not None:
            return redirect(to="project_list")

    return render(request, "pages/project/create.html")


@login_required(login_url="login")
def project_delete(request, projectID):
    project = Project.objects.get(id=projectID)

    project.delete()

    return redirect(to="project_list")


@login_required(login_url="login")
def project_edit(request, projectID):
    project = Project.objects.filter(id=projectID).first()

    context = {"project": project}

    if request.method == "POST":
        if request.FILES.get("project_image", False):
            project.image = request.FILES.get("project_image")
            project.save()
        if request.POST.get("name") != "":
            project.name = request.POST.get("name")
            project.save()
        if request.POST.get("price") != "":
            project.price = request.POST.get("price")
            project.save()
        if request.POST.get("description") != "":
            project.description = request.POST.get("description")
            project.save()
        return redirect(to="project_show", projectID=project.id)

    return render(request, "pages/project/edit.html", context)


@login_required(login_url="login")
def inbox_list(request):
    inboxes = Inbox.objects.all()
    context = {"inboxes": inboxes}

    return render(request, "pages/inbox/index.html", context)


@login_required(login_url="login")
def inbox_show(request, inboxID):
    inbox = Inbox.objects.get(id=inboxID)
    context = {"inbox": inbox}

    return render(request, "pages/inbox/show.html", context)

@login_required(login_url="login")
def inbox_destroy(request, inboxID):
    inbox = Inbox.objects.get(id=inboxID)
    inbox.delete()

    return redirect(to="inbox_list")


def inbox_create(request):
    if request.method == "POST":
        inboxData = {
            "name": request.POST.get('name'),
            'email' : request.POST.get('message'),
            'message' : request.POST.get('message')
        }
        
        Inbox.objects.create(name=inboxData['name'], email=inboxData['email'], message=inboxData['message'])
        
        return redirect(to="home")
    return redirect(to="home")

@login_required(login_url="login")
def appointment_list(request):
    
    appointments = Appointment.objects.all()
    
    context = {
        'appointments' : appointments
    }
    
    return render(request, 'pages/appointment/index.html', context)


@login_required(login_url="login")
def appointment_show(request, appointmentID):
    
    status = request.GET.get('status', None);
  
        
    appointment = Appointment.objects.get(id=appointmentID)
    
    if status is not None:
        print(appointment.Status.APPROVE)
        if status == appointment.Status.APPROVE:
            appointment.status = appointment.Status.APPROVE
            appointment.save()
        if status == appointment.Status.REJECT:
            appointment.status = appointment.Status.REJECT
            appointment.save()
    
    
    context = {
        'appointment' : appointment
    }
    
    return render(request, 'pages/appointment/show.html', context)

def appointment_create(request):
    if request.method == 'POST':
        
        appointmentData = {
            'name' : request.POST.get('name'),
            'email' : request.POST.get('email'),
            'date' : request.POST.get('date'),
            'contact_number' : request.POST.get('contact_number'),
            'project_id' : request.POST.get('project_id')
        }
        project = Project.objects.get(id=appointmentData['project_id'])
    
        
        Appointment.objects.create(
            name=appointmentData['name'],
            email=appointmentData['email'],
            date=appointmentData['date'],
            contact_number=appointmentData['contact_number'],
            project_id=project
            )
        
        return redirect(to="gallery")