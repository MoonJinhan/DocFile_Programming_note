from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index,name='index'), #crud/
    path('new/',views.new,name='new'), #crud/new 실행하기위한 것
    path('create/',views.create,name='create'), # form 데이터를 받아서 DB에 저장 할 것
    path('<int:pk>/article/',views.detail,name='detail'), #crud/pk/article/detail page
    #crud/pk/update/ 수집 체이지
    path('<int:pk>/update/',views.update,name='update'),
    path('<int:pk>/revise/',views.revise,name='revise'),
    #crud/pk/delete/ 삭제하기
    path('<int:pk>/delete/',views.delete,name='delete'),
    ]

