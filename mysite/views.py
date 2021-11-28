from django.shortcuts import render, redirect
from django.http import HttpResponse
import random
from mysite.models import VideoList
from .forms import NameForm

def index(request):
	lucky = random.randint(1, 100)
	videolists = VideoList.objects.all() #從VideoList資料表中讀取所有的記錄

	if request.method == 'POST':
		form = NameForm(request.POST)
		if form.is_valid():
			videolistname = form.cleaned_data['videolistname']
			target = VideoList(name=videolistname)
			target.save()
			return redirect("/")
	else:
		form = NameForm()

	return render(request, "index.html", locals())

def delete(request, id):
	target = VideoList.objects.get(id=id).delete()
	return redirect("/")


