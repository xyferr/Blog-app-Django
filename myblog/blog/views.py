from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post  # Post is class in database models

# Create your views here.
def home(request):
    
    posts=Post.objects.all()[:11]
    #print(posts)
    
    data={
        'posts':posts,
    }
    
    
    return render(request,'home.html',data)
