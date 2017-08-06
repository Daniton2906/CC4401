from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import Todo

# Create your views here.


def index(request):
    todos = Todo.objects.order_by('priority')
    context = {
        'name': 'Dani',
        'todos': todos
    }
    return render(request, 'index.html', context)


def details(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        'todo': todo
    }
    return render(request, 'details.html', context)


def add(request):
    if request.method == 'POST':
        task = request.POST['task']
        todo = Todo(priority=0, task=task)
        todo.save()
        new_id = todo.id
        todos = Todo.objects.exclude(id=new_id)
        for todo in todos:
            todo.priority += 1
            todo.save()
        return redirect('/')
    else:
        return render(request, 'index.html')


def removeTodo(request, id):
    old_todo = Todo.objects.get(id=id)
    old_priority = old_todo.priority
    todos = Todo.objects.filter(priority__gt=old_priority)
    for todo in todos:
        todo.priority -= 1
        todo.save()
    old_todo.delete()
    return redirect('/')


def setUpTodo(request, id):
    going_up_todo = Todo.objects.get(id=id)
    if going_up_todo.priority > 0:
        going_down_todo = Todo.objects.get(priority=going_up_todo.priority - 1)

        going_up_todo.priority -= 1
        going_down_todo.priority += 1
        going_up_todo.save()
        going_down_todo.save()

    return redirect('/')


def setDownTodo(request, id):
    going_down_todo = Todo.objects.get(id=id)
    if going_down_todo.priority < Todo.objects.count() - 1:
        going_up_todo = Todo.objects.get(priority=going_down_todo.priority + 1)

        going_up_todo.priority -= 1
        going_down_todo.priority += 1
        going_up_todo.save()
        going_down_todo.save()

    return redirect('/')