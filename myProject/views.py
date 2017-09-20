from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.
from .forms import PostForm, CommentForm
from .models import Post, Comment


def index(request):
    return render(request, 'index.html')


def blog(request):
    query_list = Post.objects.all().order_by("-timestamp")
    paginator = Paginator(query_list, 5)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        query = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        query = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        query = paginator.page(paginator.num_pages)

    context = {
        "post": query
    }
    return render(request, 'blog.html', context)


def blog_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Post is published successfully!', extra_tags='alert')
        return redirect('blog_create')

    context = {
        "form": form,
        "header":"Create a blog post"
    }
    return render(request, 'post_form.html', context)


def blog_details(request, id):
    form = CommentForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Comment is posted successfully!", extra_tags='alert')
        return redirect('blog_details', id=id)
    all_post = Post.objects.all()
    comment = Comment.objects.filter(post=id)
    last_post = Post.objects.last()
    post = get_object_or_404(Post, id=id)
    context = {
        "all_post": all_post,
        "post": post,
        "last_post": last_post,
        "comment": comment,
        "form": form
    }
    return render(request, 'single.html', context)


def blog_update(request, id=None):
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        messages.success(request, 'Post is updated successfully!', extra_tags='alert')
        return redirect('blog_details', id=id)
    context = {
        "post": post,
        "form": form,
        "header":"Update Post"
    }
    return render(request, 'post_form.html', context)


def blog_delete(request):
    return HttpResponse('This is delete page')
