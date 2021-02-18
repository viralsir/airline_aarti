from django.shortcuts import render,redirect
from .models import course_info

# Create your views here.
def insert(request):
    if request.method == 'POST':
        c=course_info(name=request.POST['name'],
                      descrition=request.POST['description'],
                      duration=request.POST['duration'],
                      fees=request.POST['Fees']
                      )
        c.save()
        return redirect('insert')
    else :
        return render(request,"course/insert.html")