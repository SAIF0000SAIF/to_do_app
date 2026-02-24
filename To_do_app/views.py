from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Task


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()

    return render(request, "register.html", {"form": form})


@login_required
def home(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")

        Task.objects.create(
            user=request.user,
            title=title,
            description=description
        )

    tasks = Task.objects.filter(user=request.user).order_by("-created_at")

    return render(request, "index.html", {"tasks": tasks})


@login_required
def delete_task(request, id):
    task = Task.objects.get(id=id, user=request.user)
    task.delete()
    return redirect("home")