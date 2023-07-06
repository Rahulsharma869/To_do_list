from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .models import Task
# Create your views here.
def index(request):
    return render(request, 'home/index.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            #login(request, user)
            return redirect('tasks')
        else:
            return HttpResponse("Invalid Credentials")
    return render(request, 'home/login.html')
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(request, 'home/signup.html', {'form': form})
def tasks(request):
    return render(request, 'home/tasks.html',{
        "tasks":Task.objects.all()
    })
def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        due_date = request.POST['due_date']
        completed = request.POST['completed']
        task = Task(title=title,description=description,due_date=due_date,completed=completed)
        task.save()
        return redirect('tasks')
    else:
        return render(request, 'home/add_task.html')