from django.shortcuts import render, redirect
from .models import Question,Choice 
import random

# Create your views here.

def index(request):
    questions = Question.objects.all()
    context={
        'questions': questions,
    }
    return render(request, 'index.html', context)

def create(request):
    if request.method =="POST":
        title=request.POST.get('title')
        question1=request.POST.get('question1')
        question2=request.POST.get('question2')

        Question.objects.create(title=title, question1=question1, question2=question2)
        return redirect('pages:index')
    else:
        return render(request, 'form.html')

def detail(request,id):
    question = Question.objects.get(id=id)
    choice1 = Choice.objects.filter(pick='1', question=question).count()
    choice2 = Choice.objects.filter(pick='2', question=question).count()
    context ={
        'question':question,
        'choice1': choice1,
        'choice2': choice2,
        'c1':choice1/(choice1+choice2)*100,
        'c2':choice2/(choice1+choice2)*100
    }
    return render(request,'detail.html',context)

def update(request,id):
    question = Question.objects.get(id=id)
    if request.method == "POST":
        title= request.POST.get('title')
        question1= request.POST.get('question1')
        question2= request.POST.get('question2')

        question.title=title
        question.question1=question1
        question.question2=question2

        question.save()
        return redirect('pages:detail', id)
    else:
        context={
            'question':question
        }
        return render(request, 'update.html', context)

def delete(request,id):
    question = Question.objects.get(id=id) 
    question.delete()

    return redirect('pages:index')

def answer_create(request, question_id):
    
    if request.method == "POST":
        question = Question.objects.get(id=question_id)
        content = request.POST.get('content')
        pick = request.POST.get('pick')
        # raise
        # print(Choice.objects.get('pick'))
        # choice = Choice.objects.get(question = question_id)
        # print(choice)
        # pick = choice.pick
        
        Choice.objects.create(content=content, pick=pick, question=question)
        # Choice.objects.create(content=content, question=question)

        
        return redirect('pages:detail', question_id)

    else:
        pass

    # return redirect('pages:detail' question.id)

def choice_delete(request,question_id,choice_id):
    choice = Choice.objects.get(id=choice_id)
    choice.delete()

    return redirect('pages:detail',question_id)

def show(request):
    question = Question.objects.all()
    rand = random.randint(0, len(question) - 1)

    return redirect('pages:detail', question[rand].id)

