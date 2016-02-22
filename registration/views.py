# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.shortcuts import render_to_response
from django.template import RequestContext

def loginRedirect(request):
	redirect_url = "/home"
	return HttpResponseRedirect(redirect_url)