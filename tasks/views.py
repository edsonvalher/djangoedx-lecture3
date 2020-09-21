from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
#tasks = ["foo", "bar", "baz"]
#tasks = []
# no such table: django_session
# python manage.py migrate


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New task")
    #priority = forms.IntegerField(label="Priority", min_value=1, max_value=8)


def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(request, "tasks/index.html", {
        # "tasks": tasks

        # en este caso estará trabajando en almacenar las variables en distintas sesiones
        "tasks": request.session["tasks"]
    })


def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            # en este caso estará trabajando en almacenar las variables en distintas sesiones
            request.session["tasks"] += [task]
            # tasks.append(task)
            return HttpResponseRedirect(reverse('tasks:index'))

        else:
            return render(request, "tasks/add.html", {
                "form": form
            })

    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })
