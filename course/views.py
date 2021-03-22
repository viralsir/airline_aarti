from django.shortcuts import render,redirect
from .models import course_info
from .forms import InserForm
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView


class NewCourse(CreateView):
    model = course_info
    fields = '__all__' # ['field1','field2''''',---,'fieldN']
    template_name = 'course/insert.html'  #form
    #success_url =



#for create and update
# modelname_form.html
class ListCourse(ListView):
    model = course_info
    context_object_name = 'courses'  #objectList
#for list
#modelname_list.html
class UpdateCourse(UpdateView):
    model = course_info
    fields = '__all__'
    template_name = "course/insert.html"

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

class CourseDelete(DeleteView):
    model = course_info
    success_url = '/course/view'

class CourseDetail(DetailView):
    model = course_info
