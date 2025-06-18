
from django.shortcuts import render, get_object_or_404
from blog.models import Post
# from django.http import Http404


# def home(request): # type: ignore
#     return render(request, "home.html") # type: ignore


# def about(request): # type: ignore
#     return render(request, "about.html") # type: ignore

def post_list(request): # type: ignore
    posts = Post.objects.all()
    return render(request, 'blog/post/list.html', {'posts': posts}) # type: ignore



def post_detail(request, id): # type: ignore
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    return render(request, 'blog/post/detail.html', {'post': post})  # type: ignore
