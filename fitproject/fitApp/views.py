from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *


# Create your views here.
def index(request):
    # return HttpResponse('시간 입력 페이지')
    # todos = Todo.objects.all()
    # content = {'todos': todos}
    exercises = Exercise.objects.all()
    content = {'exercises': exercises}
    return render(request, 'index.html', content)

def createTodo(request):
    user_input_str = request.POST['todoContent']
    new_todo = Todo(content = user_input_str)
    new_todo.save()
    return HttpResponseRedirect(reverse('index'))
    # return HttpResponse('입력한 시간 보여주기 =>'+user_input_str)

def doneTodo(request):
    done_todo_id = request.GET['todoNum']
    print('완료한 todo의 id', done_todo_id)
    todo = Todo.objects.get(id=done_todo_id)
    todo.isDone = True
    todo.save()
    return HttpResponseRedirect(reverse('index'))

def createExercise(request):
    exer_date = request.POST['exerDate']
    exer_title = request.POST['exerTitle']
    exer_time = request.POST['exerTime']
    new_exercise = Exercise(exer_date=exer_date, exer_title=exer_title, exer_time=exer_time)
    new_exercise.save()
    return HttpResponseRedirect(reverse('index'))
    # return HttpResponse('운동종류: '+exer_title+'운동시간: '+exer_time)

def deleteExercise(request):
    delete_exercise_id = request.GET['exerNum']
    print('삭제할 exercise의 id', delete_exercise_id)
    exercise = Exercise.objects.get(id=delete_exercise_id)
    exercise.delete()
    return HttpResponseRedirect(reverse('index'))

def bar(request):
    a = [107, 31, 635, 203]
    b = [133, 156, 947, 408]
    c = [814, 841, 714, 727]
    d = [216, 1001, 436, 738]

    context = {'a' : a, 'b' : b, 'c' : c, 'd' : d}

    return render(request, 'chart_bar.html', context)