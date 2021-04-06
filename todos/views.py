from .models import Item, TodoForm
from django.contrib.auth.models import User
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.utils.decorators import method_decorator
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, reverse


@method_decorator(login_required, name='get')
class TodosView(generic.ListView):
    template_name = 'todos/index.html'
    context_object_name = 'items'
    paginate_by = 3

    def get_queryset(self):
        return Item.objects.filter(user__id=self.request.user.id).order_by('-pub_date')

@method_decorator(login_required, name='get')
class SingleTodo(generic.DetailView):
    model = Item
    template_name = 'todos/edit.html'


def changeTodo(request, todo_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            todo = get_object_or_404(Item, pk=todo_id)
            todo.name = request.POST['todo_name']
            if request.POST['todo_descr'] == '':
                todo.descr = None
            else:
                todo.descr = request.POST['todo_descr']
            todo.is_completed = request.POST['todo_complete']
            todo.save()
            return HttpResponseRedirect(reverse('todos:index', args=()))
    else:
        return HttpResponseRedirect('/TodoApp/')


def deleteTodo(request, todo_id):
    if request.user.is_authenticated:
        todo = get_object_or_404(Item, pk=todo_id)
        todo.delete()
        return HttpResponseRedirect(reverse('todos:index', args=()))
    else:
        return HttpResponseRedirect('/TodoApp/')

def AddTodo(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = TodoForm()
            return render(request, 'todos/addtodo.html', {'form':form})
        else:
            form = TodoForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                descr = form.cleaned_data['descr']
                is_complete = form.cleaned_data['is_completed']
                new_form = Item(name=name, descr=descr, is_completed=is_complete, user=request.user)
                new_form.save()
                return HttpResponseRedirect(reverse('todos:index', args=()))
    else:
        return HttpResponseRedirect('/TodoApp/')

def new_user(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        if User.objects.filter(username=user_name).exists():
            return render(request, 'todos/addUser.html', {'error':'Username has been taken'})
        else:
            new_user = User.objects.create_user(user_name, email, password)
            new_user.first_name = first_name
            new_user.last_name = last_name
            new_user.save()
            return HttpResponseRedirect('/TodoApp/')
    else:
        return render(request, 'todos/addUser.html')