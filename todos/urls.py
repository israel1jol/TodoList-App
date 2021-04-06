from django.urls import path
from . import views as todoviews
from django.contrib.auth import views

app_name = 'todos'
urlpatterns = [
    path('', views.LoginView.as_view(template_name='todos/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('home/',todoviews.TodosView.as_view(), name='index'),
    path('edit/<int:pk>/', todoviews.SingleTodo.as_view(), name='edit'),
    path('edit/<int:todo_id>/change/', todoviews.changeTodo, name='change'),
    path('home/<int:todo_id>/delete/', todoviews.deleteTodo, name='delete'),
    path('addTodo/', todoviews.AddTodo, name='addTodo'),
    path('signUp/', todoviews.new_user, name='addUser')
]
