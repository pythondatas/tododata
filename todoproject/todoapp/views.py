from django.shortcuts import render,redirect
from django.http import HttpResponse
from . forms import taskform

from .models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.
class TaskListView(ListView):
    model=Task
    template_name='home.html'
    context_object_name='data'
class TaskDetailview(DetailView):
    model=Task
    template_name='details.html'
    context_object_name='data2'

class TaskUpdateview(UpdateView):
    model=Task
    template_name='cbupdate.html'
    context_object_name='data3'
    fields=('name','priority','date')


class TaskDeleteview(DeleteView):
    model=Task
    template_name='delete.html'
    success_url=reverse_lazy('chome')


    def get_success_url(self):
        return reverse_lazy('cdetails',kwargs={'pk':self.object.id})



def function(request):
    data=Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'data':data})

# def details(request):
#     return render(request,'details.html')

def delete(request,taskid):
    if request.method=='POST':
        task1=Task.objects.get(id=taskid)
        task1.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    task2=Task.objects.get(id=id)
    form2=taskform(request.POST or None, instance=task2)
    if form2.is_valid():
        form2.save()
        return redirect('/')
    return render(request,'update.html',{'task2':task2,'form2':form2})