from django.shortcuts import render
# import cx_Oracle as o

# 리다이렉트 시 사용
from django.http import HttpResponseRedirect
from django.urls import reverse


# 에러 발생 시

#This is the django module which allows the Django object to become JSON
from django.core import serializers

# for csv to DB
# import pandas as pd

def index(request):
    return render(request, 'index.html')

def opinion(request):
    return render(request, 'board/opinion.html')

def insert(request):
    return render(request, 'board/insert.html')

def insertOpinion(request):
    region = request.args['region']
    place = request.args['place']
    reason = request.args['reason']
    say = request.args['say']
    rst = insertdata(region,place,reason,say)
    return rst

def see(request):
    data = selectdata()
    print(data)
    return render('see.html', data=data)

def insertdata(region, place, reason,say):
    try:
        sql = "insert into famous values(:region, :place,:reason,:say)" # 입력될 테이블명선언
        dsn = o.makedsn('localhost','1521', 'xe')
        conn = o.connect(user='hr',password='hr',dsn=dsn)
        cur = conn.cursor()
        cur.execute( sql, (region,place,reason,say))
        conn.commit()
        conn.close()
        return "의견 감사합니다!"
    except Exception as err:
        print('err:',err)
        return '입력에 실패했습니다.'

def selectdata():
    try:
        sql = "select * from famous" # 불러올 테이블 명
        dsn = o.makedsn('localhost','1521', 'xe')
        conn = o.connect(user='hr',password='hr',dsn=dsn)
        cur = conn.cursor()
        cur.execute( sql )

        data = cur.fetchall()
        conn.close()
        return data

    except Exception as err:
        print('err:',err)
        return None