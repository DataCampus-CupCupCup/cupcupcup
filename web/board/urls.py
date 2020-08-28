from django.urls import path
from board import views

urlpatterns = [
    # 첫 페이지 page
    path('', views.opinion, name='opinion'),
    path('insert/', views.insert, name='insert'),
    path('insertOpinion/', views.insertOpinion, name='insertOpinion'),
    # path('see/', views.see, name='see'),
    path('insertdata/', views.insertdata, name='insertdata'),
    path('selectdata/', views.selectdata, name='selectdata')
]