from django.shortcuts import render

# 리다이렉트 시 사용
from django.http import HttpResponseRedirect
from django.urls import reverse
# ajax 응답
from django.http import HttpResponse

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

def login(request):
    return render(request, 'login.html')

def logout(request):
    request.session.flush()
    return HttpResponseRedirect(reverse(index))

def check_account(request):
    request.session['auth'] = 1
    return manage(request)

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

def check_login(function):
    def wrapper(request, *args, **kwargs):
        auth = request.session.get('auth',0)
    
        if auth == 0 : return login(request)
        else : return function(request, *args, **kwargs)
    return wrapper

@check_login
def manage(request, gu='서초구'):
    id_start = 's'
    if gu=='서대문구': id_start = 'sd'
    elif gu=='강남구' :  id_start = 'gn'

    predictCups = list(PredictCup.objects.filter(id__startswith=id_start).values())
    presentCups = list(PresentCup.objects.filter(id__startswith=id_start).values())

    context = { "presentCups" : presentCups, 'cnt1' : len(presentCups), 'predictCups': predictCups, 'cnt2': len(predictCups)}

    return render(request, 'citizen/manage.html', context)

def post_like(request):
    id = request.POST.get('id', None) # ajax 통신을 통해서 template에서 POST방식으로 전달
    label = request.POST.get('label', None) # ajax 통신을 통해서 template에서 POST방식으로 전달

    row = None
    if label == 'predictCups': row = PredictCup.objects.get(id=id)
    else : row = PresentCup.objects.get(id=id)

    row.like += 1
    row.save()

    context = {'like_count': row.like }
    
    return HttpResponse(json.dumps(context), content_type="application/json")
    # context를 json 타입으로

def post_dislike(request):
    id = request.POST.get('id', None) # ajax 통신을 통해서 template에서 POST방식으로 전달
    label = request.POST.get('label', None) # ajax 통신을 통해서 template에서 POST방식으로 전달

    row = None
    if label == 'predictCups': row = PredictCup.objects.get(id=id)
    else : row = PresentCup.objects.get(id=id)

    row.dislike += 1
    row.save()
    
    context = {'dislike_count': row.dislike }
    
    return HttpResponse(json.dumps(context), content_type="application/json")
    # context를 json 타입으로
    

        

# csv to DB
# def insert(request):
#     df = pd.read_csv('./citizen/final_presentcup.csv', encoding='utf-8')

#     df.apply(makePresentCup, axis=1)

#     print(PresentCup.objects.all())
#     return render(request, 'index.html')

# def makePresentCup(df):
#     ['lat', 'long', 'id', 'like', 'address', 'dislike']
#     pc_instance = PresentCup(id=df.id, long=df.long, lat= df.lat, address=df.address, dislike=df.dislike, like=df.like)
#     pc_instance.save()

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
