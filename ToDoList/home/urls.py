from django.urls import path
from . import views
 
urlpatterns = [
    path("", views.index, name='index'),
    path("login/", views.login, name='login'),
    path("signup/", views.signup, name='signup'),
    path("tasks/", views.tasks, name='tasks'),
    path("add/", views.add_task, name='add_task')
]
