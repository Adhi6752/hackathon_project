from django.shortcuts import get_object_or_404, redirect, render

from posts.models import Post
# Create your views here.
def detail(request,slug):
    post=get_object_or_404(Post,slug=slug)
    return render(request,'detail.html',{'post':post})
