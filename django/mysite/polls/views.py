from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.

def index (request):
    return HttpResponse('Pham Quoc Hoang')

def index2 (request):
    name = 'Phạm Quốc Hoàng'
    age = '19'
    address ='Quảng Ngãi'
    phone = '0123456789'
    courses = ['Java','PHP','Python','HTML']
    result = {'name':name,'age':age,'address':address,'phone':phone,'courses':courses}
    return render(request,'polls/index.html',result)


def viewlist(request):
    list_question = Question.objects.all()
    result = {'dsquest':list_question}
    return render(request,'polls/question_list.html',result)

def detailview(request,question_id):
    q = Question.objects.get(pk= question_id)
    return render(request,'polls/detail_question.html',{'qs':q})



def vote(request,question_id):
    q = Question.objects.get(pk=question_id)
    try:
        dulieu = request.POST["choice"]
        c=q.choice_set.get(pk=dulieu)
    except:
        HttpResponse ("Lỗi không có choice")
    c.vote = c.vote+1
    c.save()
    
    return render (request,"polls/result.html",{'q':q})
