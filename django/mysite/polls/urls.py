from django.urls import path
from . import views


app_name = 'polls'
urlpatterns = [
    path('' ,views.index,name='index'),
    path('index2/' ,views.index2,name='index2'),
    path('list/' ,views.viewlist,name='view_list'),
    path('detail/<int:question_id>/',views.detailview,name='detail'),
    path('<int:question_id>', views.vote,name='vote'),
]
