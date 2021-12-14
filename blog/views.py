from django.shortcuts import render

from .models import Post

def home(request):
    data = Post.objects.all()
    return render(request, "index.html", {"posts":data})

def insert(request):
    data_inserted = Post.objects.update()
    return render(request, "insert.html", {"insert.html":data_inserted})