from django.urls import path
from .import views
app_name='posts'
urlpatterns=[
	path('',views.get_news,name='get_news'),

]