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
    # sum_time = Exercise.objects.filter(exer_date__month=9).aggregate(Sum('exer_time'))
    # print(sum_time)





    sujin_time10 = Exercise.objects.filter(nickname='수진', exer_date__month=10).aggregate(Sum('exer_time'))
    sujin10 = sujin_time10['exer_time__sum']


    # sujin_time9 = Exercise.objects.filter(nickname='sujin', exer_date__month=9).aggregate(Sum('exer_time'))
    # sujin9 = sujin_time9['exer_time__sum']
    # print(sujin_time9)

    nayoung_time10 = Exercise.objects.filter(nickname='나영', exer_date__month=10).aggregate(Sum('exer_time'))
    nayoung10 = nayoung_time10['exer_time__sum']

    jihee_time10 = Exercise.objects.filter(nickname='지희', exer_date__month=10).aggregate(Sum('exer_time'))
    jihee10 = jihee_time10['exer_time__sum']


    heejung_time10 = Exercise.objects.filter(nickname='희정', exer_date__month=10).aggregate(Sum('exer_time'))
    heejung10 = heejung_time10['exer_time__sum']


    jinhee_time10 = Exercise.objects.filter(nickname='진희', exer_date__month=10).aggregate(Sum('exer_time'))
    jinhee10 = jinhee_time10['exer_time__sum']
    print(jinhee_time10)





    a = [sujin10] # 수진 = [10월, 9월, 8월, 7월]
    b = [nayoung10] # 나영
    c = [jihee10] # 지희
    d = [heejung10] # 희정
    e = [jinhee10] # 진희

    context = {'a': a, 'b': b, 'c': c, 'd': d, 'e': e,'exercises': exercises}

    return render(request, 'chart_bar.html', context)


