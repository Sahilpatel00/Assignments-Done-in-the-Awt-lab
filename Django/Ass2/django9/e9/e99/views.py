from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User

def user_form(request):
    # if request.method == 'GET':
    #     forrm=User()
    #     forrm.name=request.GET.get['name']
    #     forrm.name=request.GET.get['email']
    #     forrm.name=request.GET.get['address']
    #     forrm.name=request.GET.get['hobby']
    #     forrm.save()
        
    # print("helloo")

    return render(request, 'user_form.html')


def user_list(request):
    
    users = User.objects.all()
    print(users)
    return render(request, 'user_view.html', {'users': users})


def thank(request):

    forrm=User()
    
    forrm.name=request.POST['name']
    forrm.email=request.POST['email']
    forrm.address=request.POST['address']
    forrm.hobby=request.POST['hobby']
    
    forrm.save()
       
        
    return render(request,'thank.html')
    