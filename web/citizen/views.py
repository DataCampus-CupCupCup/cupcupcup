from django.shortcuts import render

# 리다이렉트 시 사용
from django.http import HttpResponseRedirect
from django.urls import reverse

# 모델 불러오기
from .models import PresentCup, PredictCup

# 에러 발생 시

#This is the django module which allows the Django object to become JSON
from django.core import serializers

# for csv to DB
import pandas as pd
import json

def index(request):
    return render(request, 'index.html')

def map(request):
    return render(request, 'maps.html')

def our_team(request):
    return render(request, 'maker.html')

def citizen_map(request, gu='서초구'):
    id_start = 's'
    if gu=='서대문구': id_start = 'sd'
    elif gu=='강남구' :  id_start = 'gn'

    predictCups = list(PredictCup.objects.filter(id__startswith=id_start).values())
    presentCups = list(PresentCup.objects.filter(id__startswith=id_start).values())

    context = { "presentCups" : presentCups, 'cnt1' : len(presentCups), 'predictCups': predictCups, 'cnt2': len(predictCups)}

    return render(request, 'citizen/citizen_maps.html', context)

def manage(request, gu='서초구'):
    id_start = 's'
    if gu=='서대문구': id_start = 'sd'
    elif gu=='강남구' :  id_start = 'gn'

    predictCups = list(PredictCup.objects.filter(id__startswith=id_start).values())
    presentCups = list(PresentCup.objects.filter(id__startswith=id_start).values())

    context = { "presentCups" : presentCups, 'cnt1' : len(presentCups), 'predictCups': predictCups, 'cnt2': len(predictCups)}

    return render(request, 'citizen/manage.html', context)
    

# csv to DB
# def insert(request):
#     df = pd.read_csv('./citizen/sucho_cup_DB_detail_address.csv', encoding='utf-8')

#     df.apply(makePresentCup, axis=1)

#     print(PresentCup.objects.all())
#     return render(request, 'maps.html')

# def makePresentCup(df):
    # ['lat', 'long', 'id', 'like', 'address', 'dislike']
    # pc_instance = PresentCup(id=df.id, long=df.long, lat= df.lat, address=df.address, dislike=df.dirty, like=df.like)
    # pc_instance.save()


# 예측
# def insert(request):
#     df = pd.read_csv('./citizen/gangnam_predict.csv', encoding='EUC-KR')

#     df.apply(makePredictCup, axis=1)

#     print(PredictCup.objects.all())
#     return render(request, 'maps.html')

# def makePredictCup(df):
#     # ['id', lat1', 'long1','lat2', 'long2','lat3', 'long3','lat4', 'long4', 'id', 'dislike','like', 'address']
#     pc_instance = PredictCup(id=df.id, long1=df.long1, lat1= df.lat1,long2=df.long2, lat2= df.lat2, long3=df.long3, lat3= df.lat3, long4=df.long4, lat4= df.lat4, address=df.address, dislike=df.dislike, like=df.like)
#     pc_instance.save()
