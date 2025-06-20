from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.http import Http404


# def home(request): # type: ignore
#     return render(request, "home.html") # type: ignore


# def about(request): # type: ignore
#     return render(request, "about.html") # type: ignore


def post_list(request): # type: ignore
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 3)  # Show 3 posts per page.
    page_number = request.GET.get('page', 1)

    try: # type: ignore
        posts = paginator.get_page(page_number) # type: ignore
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.get_page(1) # type: ignore
    except EmptyPage:
        posts = paginator.get_page(paginator.num_pages)
    
    return render(request, 'blog/post/list.html', {'posts': posts}) # type: ignore



def post_detail(request, year, month, day, slug): # type: ignore
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED
                            , publish__year=year
                            , publish__month=month
                            , publish__day=day
                            , slug=slug
                            )
    return render(request, 'blog/post/detail.html', {'post': post})  # type: ignore
