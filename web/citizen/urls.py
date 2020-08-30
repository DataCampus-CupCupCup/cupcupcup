from django.urls import path
from citizen import views

urlpatterns = [
    # 첫 페이지 page
    path('', views.index, name='home'),
    path('our_team/', views.our_team, name='our_team'),
    path('map/', views.map, name='map'),
    path('citizen_map/', views.citizen_map, name='citizen_map'),
    path('citizen_map/<str:gu>/', views.citizen_map, name='citizen_map_search'),
    path('manage/', views.manage, name='manage'),
    path('manage/<str:gu>/', views.manage, name='manage_search'),
    path('our_team/', views.our_team, name='our_team'),
    path('post_like/', views.post_like, name='post_like'),
    path('post_dislike/', views.post_dislike, name='post_dislike'),
    # path('insert/', views.insert, name='insert'),
]