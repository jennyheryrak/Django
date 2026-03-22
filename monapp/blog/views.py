from django.shortcuts import render
from .models import Post

# Create your views here.
# localhost:8000/blog?nom=Testeur
def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})