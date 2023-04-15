from django.shortcuts import render, HttpResponse
 
from home.models import info     # added later



# Create your views here.
def index(request):
    return HttpResponse("This is homepage")
def about(request):
    return HttpResponse("This is about page")
def sample(request):    # for templates
     #  if webpage is with variable passing
     context ={     
      'variable':'This is the value for variable'
     }
     return render(request, 'firstpage.html',context)
    
    
    #if only webpage is there without variables
    #return render(request, 'firstpage.html')
    
def form(request):    # for templates
     ####Logic for form submission
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        obj = info(name=name,email=email,phone=phone,desc=desc)
        obj.save()

     #########################
    return render(request, 'forminfo.html')
    

