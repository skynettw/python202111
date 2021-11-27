from django.shortcuts import render
from django.http import HttpResponse
import random
from mysite.models import VideoList

def index(request):
	lucky = random.randint(1, 100)
	videolists = VideoList.objects.all() #從VideoList資料表中讀取所有的記錄
	return render(request, "index.html", locals())


