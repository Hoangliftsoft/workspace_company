from django.urls import path
from . import views

app_name = "myclass"
urlpatterns = [
    path('class1/',views.class1,name="class1"),
    path('class2/',views.class2,name="class2"),
    path('class3/',views.class3,name="class3"),
    path('class4/',views.class4,name="class4"),
    path('qlist/',views.view_question,name="view_question"),
    path('detail/<int:question_id>',views.detailView,name="detailView"),
    path('<int:question_id>',views.vote,name="vote"),
] 