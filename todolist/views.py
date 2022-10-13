from django.shortcuts import render
from django.shortcuts import redirect
from todolist.models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core import serializers
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@login_required(login_url='/todolist/login/')
def show_todolist(request):
    context = {
        'user': request.user,
    }
    return render(request, 'todolist.html', context)


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')

    context = {'form': form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # melakukan login terlebih dahulu
            response = HttpResponseRedirect(
                reverse("todolist:show_todolist"))  # membuat response
            # membuat cookie last_login dan menambahkannya ke dalam response
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response


@csrf_exempt
@login_required(login_url='/todolist/login/')
def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        todo = Task.objects.create(
            user=request.user,
            title=title,
            description=description,
            is_finished=False,
            date=datetime.datetime.today())
        return JsonResponse(
            {
                'pk': todo.id,
                'fields': {
                    'title': todo.title,
                    'description': todo.description,
                    'is_finished': todo.is_finished,
                    'date': todo.date,
                },
            },
            status=200,
        )

@login_required(login_url='/todolist/login/')
def update_task(request, id):
    todo = Task.objects.get(user=request.user, id=id)
    todo.is_finished = not todo.is_finished
    todo.save()
    return redirect('todolist:show_todolist')


@login_required(login_url='/todolist/login/')
def delete_task(request, id):
    todo = Task.objects.get(user=request.user, id=id)
    todo.delete()
    return redirect('todolist:show_todolist')


@login_required(login_url='/todolist/login/')
def get_todo_json(request):
    todo = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", todo), content_type="application/json")
