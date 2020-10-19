from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    # path('createTodo/', views.createTodo, name='createTodo'),
    path('doneTodo/', views.doneTodo, name='doneTodo'),
    path('createExercise/', views.createExercise, name='createExercise'),
    path('deleteExercise/', views.deleteExercise, name='deleteExercise'),
    path('', views.bar, name='bar')
]