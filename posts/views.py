from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def get_news(request):
	url='http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=33a794feb0c24d07810406fa7dc3e978'
	data=requests.get(url)
	d=data.json()

	
	return render(request,'home.html',{'data':d})