from django.shortcuts import render

# 리다이렉트 시 사용
from django.http import HttpResponseRedirect
from django.urls import reverse

# 모델 불러오기
from .models import PresentCup

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

def citizen_map(request, gu='서초구'):
    id_start = 's'
    df = pd.read_csv('./citizen/real_seocho.csv', encoding='utf-8')
    df = json.dumps(df.head().to_dict('index'))

    qs = PresentCup.objects.filter(id__startswith=id_start)
  
    # javascript 에서 사용하기 위해 json으로 줄것
    json_data = serializers.serialize('json', qs)

    # context = { "pc" : json_data }

    context = { "pc" : json_data, 'count' : len(qs), 'df': df}

    return render(request, 'citizen/citizen_maps.html', context)
    

# csv to DB
# def insert(request):
#     df = pd.read_csv('./citizen/sucho_cup_DB_detail_address.csv', encoding='utf-8')

#     df.apply(makePresentCup, axis=1)

#     print(PresentCup.objects.all())
#     return render(request, 'maps.html')

# def makePresentCup(df):
#     # ['lat', 'long', 'id', 'dirty', 'address']
#     pc_instance = PresentCup(id=df.id, long=df.long, lat= df.lat, address=df.address, dirty=df.dirty)
#     pc_instance.save()
