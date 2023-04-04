from django.shortcuts import render ,redirect
from .models import blog
from django.http import HttpResponse

# Create your views here.


def home(request):
    blogs = blog.objects.all()
    context={
        'blogs': blogs
    }
    return render(request,'home.html',context)

def add_blog(request):
    if request.method== "POST":
        name = request.POST['name']
        details = request.POST['details']
        newblog= blog(name=name, details=details)
        newblog.save()
        return redirect('/')
    elif request.method =='GET':
            return render(request,'home.html')
        
    else:
            return HttpResponse("Error!")