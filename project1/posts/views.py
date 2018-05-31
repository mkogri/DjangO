from django.shortcuts import render
from django.http import HttpResponse

from .models import Posts

# Create your views here.
def index(request) :
	#return HttpResponse('Hello from posts')
    posts = Posts.objects.all()[:10]
    # to pass our data to our template
    context = {
    'title': 'Latest posts',
    'posts': posts
   }
    return render(request, 'posts/index.html', context)
    
def details(request, id) :
    post = Posts.objects.get(id=id)
    context = {
        'post': post
    }
    return render(request, 'posts/details.html', context)

'''
    return render(request, 'posts/index.html',{
        'title': 'Latest post'
    })
'''