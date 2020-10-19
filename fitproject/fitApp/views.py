from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *
from django.db.models import Sum


# Create your views here.
def index(request):
    # return HttpResponse('시간 입력 페이지')
    # todos = Todo.objects.all()
    # content = {'todos': todos}
    exercises = Exercise.objects.all()
    content = {'exercises': exercises}
    return render(request, 'index.html', content)


def doneTodo(request):
    done_todo_id = request.GET['todoNum']
    print('완료한 todo의 id', done_todo_id)
    todo = Todo.objects.get(id=done_todo_id)
    todo.isDone = True
    todo.save()
    return HttpResponseRedirect(reverse('index'))

def createExercise(request):
    nickname = request.POST['nickname']
    exer_date = request.POST['exerDate']
    exer_title = request.POST['exerTitle']
    exer_time = request.POST['exerTime']
    new_exercise = Exercise(nickname=nickname, exer_date=exer_date, exer_title=exer_title, exer_time=exer_time)
    new_exercise.save()
    return HttpResponseRedirect(reverse('bar'))
    # return HttpResponse('운동종류: '+exer_title+'운동시간: '+exer_time)

def deleteExercise(request):
    delete_exercise_id = request.GET['exerNum']
    print('삭제할 exercise의 id', delete_exercise_id)
    exercise = Exercise.objects.get(id=delete_exercise_id)
    exercise.delete()
    return HttpResponseRedirect(reverse('bar'))

def bar(request):
    exercises = Exercise.objects.all()
    sum_time = Exercise.objects.all().aggregate(Sum('exer_time'))
    tt = sum_time['exer_time__sum']
    print(tt)


    a = [tt, 130] # 수진 = [10월, 9월, 8월, 7월]
    b = [133, 156]
    c = [814, 841]
    d = [216, 1001]

    context = {'a' : a, 'b' : b, 'c' : c, 'd' : d, 'exercises': exercises}

    return render(request, 'chart_bar.html', context)