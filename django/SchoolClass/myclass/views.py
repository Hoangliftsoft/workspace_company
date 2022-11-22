from django.shortcuts import render
from .models import Question
from django.http import HttpResponse
# Create your views here.

def class1(request):
    list_student = ["class1-student1","class1-student2","class1-student3","class1-student4","class1-student5"]
    result = {'list_class1':list_student}
    return render(request,"myclass/index.html",result)

def class2(request):
    list_student = ["class2-student1","class2-student2","class2-student3","class2-student4","class2-student5"]
    result = {'list_class2':list_student}
    return render(request,"myclass/class2.html",result)

def class3(request):
    list_student = ["class3-student1","class3-student2","class3-student3","class3-student4","class3-student5"]
    result = {'list_class3':list_student}
    return render(request,"myclass/class3.html",result)

def class4(request):
    list_student = ["class4-student1","class4-student2","class4-student3","class4-student4","class4-student5"]
    result = {'list_class4':list_student}
    return render(request,"myclass/class4.html",result)

def view_question(request):
    # question_list = get_list_or_404(Question,pk = 1)
    question_list = Question.objects.all()
    result = {'question_list':question_list}
    return render(request,"myclass/question_list.html",result)

def detailView(request,question_id):
    q=Question.objects.get(pk = question_id)
    return render(request,"myclass/detail_question.html",{'detail_list':q})

def vote(request,question_id):
    q = Question.objects.get(pk = question_id)
    try:
        dulieu = request.POST["choice"]
        c = q.choice_set.get(pk = dulieu)
    except:
        HttpResponse("Lỗi không có choice!")
    c.choice_vote  =  c.choice_vote + 1
    c.save()
    return render(request,"myclass/result.html",{"q":q})
