from django.shortcuts import render, redirect,HttpResponse
from .models import *
from django.contrib import messages

def index(request):
    return render(request, "good_app/index.html")
def success(request):
    if (request.session.has_key("userid")):
        context={
            "user": User.objects.get(id=request.session["userid"])
                }
    return render(request, "good_app/success.html",context)
def register(request):
    if request.method == "POST":
        errors = User.objects.register_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            user=User.objects.create(name=request.POST["name"],email=request.POST["email"], pw_hash=request.POST["pw_hash"])
            request.session['userid'] = user.id
            return redirect('/success')
    return render(request, 'good_app/index.html')
def login(request):
    if request.method == "POST":
        errors = User.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            user=User.objects.get(email=request.POST["email"], pw_hash=request.POST["pw_hash"])
            request.session['userid'] = user.id
            return redirect('/success')
    return render(request, 'good_app/index.html')
def logout(request):
    request.session.clear()
    return render(request, "good_app/index.html")
def addPage(request):
    return render(request, "good_app/add.html")
def appointments(request):
    if (request.session.has_key("userid")):
        context={
            "user": User.objects.get(id=request.session["userid"]),
            "appointments":Appointment.objects.filter(user=int(request.session["userid"]))
                }
    print(appointments)
    return render(request, "good_app/appointments.html", context)
def delete(request, id):
    appointment=Appointment.objects.get(id=id)
    appointment.delete()
    return redirect('/appointments')
def edit(request, id):
    print('edit', id)
    context = {
            "appointment":Appointment.objects.get(id=id)
        }
    print('edit', "appointment",Appointment.objects.get(id=id))
    return render(request,"good_app/edit.html",context)

def addApp(request):
    if request.method == "POST":
            user=User.objects.get(id=request.session["userid"])
            errors = Appointment.objects.appointment_validator(request.POST)
            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request, value)
                return redirect('/addPage')
            else:
                appointment=Appointment.objects.create(task=request.POST["task"],date=request.POST["date"],status=request.POST["status"],user=user) 
                request.session['appointmentid'] = appointment.id
                print(appointment)
            return redirect('/appointments')
def update(request, id):
    if request.method=="POST":
        user=User.objects.get(id=request.session["userid"])
        errors = Appointment.objects.appointment_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/edit/'+id)
        else:   
            appointment = Appointment.objects.get(id = id)
            appointment.task = request.POST['task']
            appointment.date = request.POST['date']
            appointment.status = request.POST['status']
            appointment.save()
            return redirect('/appointments')