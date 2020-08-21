from django.urls import path
from citizen import views

urlpatterns = [
    # 첫 페이지 page
    path('', views.index, name='home'),
    path('map/', views.map, name='map'),
]