from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def get_news(request):
	url='http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=33a794feb0c24d07810406fa7dc3e978'
	r=requests.get(url).json()
	

	context_data={
	'author':r['articles'][0]['author'],
	'title':r['articles'][1]['title'],
	'url':r['articles'][3]['url'],
	'urlToImage':r['articles'][4]['urlToImage'],
	'publishedAt':r['articles'][5]['publishedAt'],
	
	}
	i=context_data.articles
	for item in i:
		print(item)
	

	return render(request,'home.html')