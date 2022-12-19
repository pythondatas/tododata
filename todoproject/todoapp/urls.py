from . import views
from django.urls import path,include

urlpatterns = [

    path('',views.function,name='function'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('chome/',views.TaskListView.as_view(),name='chome'),
    path('cdetails/<int:pk>/',views.TaskDetailview.as_view(),name='cdetails'),
    path('cbupdate/<int:pk>/',views.TaskUpdateview.as_view(),name='cbupdate'),
    path('cdelete/<int:pk>/',views.TaskDeleteview.as_view(),name='cdelete'),
]
