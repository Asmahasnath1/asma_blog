from django.urls import path
from  .views  import  PostBlog,Home,About

app_name = 'blog'

urlpatterns =[ 
		path('postblog/',PostBlog,name='postblog'),
		path('home/',Home,name='home'),
		path('about/',About,name='about'),




]