from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User

def user_form(request):
    if request.method == 'POST':
        forrm=User()
        forrm.name=request.POST.get['name']
        forrm.name=request.POST.get['email']
        forrm.name=request.POST.get['address']
        forrm.name=request.POST.get['hobby']
        forrm.save()
        
    print("helloo")
    return render(request, 'user_form.html')


def user_list(request):
    users = User.objects.all()
    print(users)
    return render(request, 'user_view.html', {'users': users})