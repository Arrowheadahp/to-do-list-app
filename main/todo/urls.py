from django.urls import path

from .views import index, add_task, del_task

app_name = 'todo' 

urlpatterns = [
    path('', index.as_view(), name ='index'),
    path('add_task/', add_task, name ='add_task'), 
    path('del_task/<int:pk>', del_task, name ='del_task')
]