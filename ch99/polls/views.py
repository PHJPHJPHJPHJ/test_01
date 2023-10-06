from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('안녕하세요 polls index 홈페이지에 오신 것을 환영합니다.')
