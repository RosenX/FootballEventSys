from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

def homepageView(request):
	context={}
	return render(request,"home/homepage.html",context)