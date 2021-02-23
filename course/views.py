from django.shortcuts import render,redirect
from .models import course_info
from .forms import InserForm
from django.views.generic import CreateView


class NewCourse(CreateView):
    model = course_info
    fields = '__all__'
    template_name = 'course/insert.html'

# <modelname>_form.html
# course_info_form.html


# Create your views here.
def insert(request):
    if request.method == 'POST':
        form=InserForm(request.POST)
        if form.is_valid():
            form.save()
            # c=course_info(name=request.POST['name'],
            #           descrition=request.POST['description'],
            #           duration=request.POST['duration'],
            #           fees=request.POST['Fees']
            #           )
            # c.save()
        return redirect('insert')
    else :
        form=InserForm()
        return render(request,"course/insert.html",{
            "form":form
        })