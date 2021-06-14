from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

# Create your views here.
from .models import task
from django.views.generic import ListView
from django.utils import timezone
from django.urls import reverse

class index(ListView):
    queryset = task.objects.all().order_by('-date_added')
    context_object_name = 'task_list'

    template_name = 'todo/index.html'


def add_task(request):
    newtask = request.POST['newtask']
    task.objects.create(text=newtask, date_added= timezone.now())

    return HttpResponseRedirect(reverse('todo:index'))

def del_task(request, pk):
    obj = get_object_or_404(task, id=pk)
    if request.method == 'POST':
        obj.delete()
    
    return HttpResponseRedirect(reverse('todo:index'))