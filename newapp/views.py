from django.shortcuts import render,HttpResponse,redirect
from .models import Student

# Create your views here.


def register(request):
    
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        mob=request.POST['number']

        data=Student.objects.create(name=name,email=email,number=mob)
        data.save()


    return render(request,'register.html')

def dashpanel(request):
    data=Student.objects.all()

    return render(request,'dashpannel.html',{'data':data})

def datadelete(request,id):
    data=Student.objects.filter(id=id)
    data.delete()
    return render(request,'dashpannel.html')

 
def dataedit(request,id):
    data=Student.objects.filter(id=id)
    if request.method=='POST':
        sid=request.POST['sid']
        name=request.POST['name']
        email=request.POST['email']
        num=request.POST['number']
        if "@" in email:

            data.update(name=name,email=email,number=num)
            return redirect('dashpanel')
    
        else:
            return HttpResponse('Enter the valid Email')
        
    return render(request,'edit.html',{'data':data})    


        

