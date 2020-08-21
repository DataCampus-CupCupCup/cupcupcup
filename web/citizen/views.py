from django.shortcuts import render

# 리다이렉트 시 사용
from django.http import HttpResponseRedirect
from django.urls import reverse

# 나중에 모델 불러올 때

# 에러 발생 시


def index(request):
    return render(request, 'index.html')

def map(request):
    return render(request, 'maps.html')
