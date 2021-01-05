from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
# Create your views here.
def data(request):
	url='http://newsapi.org/v2/everything?q=bitcoin&from=2020-12-05&sortBy=publishedAt&apiKey=33a794feb0c24d07810406fa7dc3e978'
	data=requests.get(url).json()
	return HttpResponse(data)