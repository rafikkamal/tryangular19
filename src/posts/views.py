from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Created Post!!!", extra_tags="bg-success")
        return redirect('posts:index')
    elif request.method == 'POST':
        messages.success(request, "Error: No Post Created!!!", extra_tags="bg-danger")

    # if request.method == 'POST':
    #     post = Post()
    #     post.title = request.POST['title']
    #     post.content = request.POST['content']
    #     post.save()
    #     return redirect('posts:index')

    context = {
        'title': 'Create Post',
        "form": form,
    }
    return render(request, 'posts/post_form.html', context)


def post_detail(request, id=None):
    queryset = Post.objects.get(id=id)
    context = {
        'post': queryset,
    }
    return render(request, 'posts/detail.html', context)


def post_list(request):
    queryset = Post.objects.all()
    context = {
        'posts': queryset,
        'title': 'Index',
    }
    return render(request, 'posts/index.html', context)


def post_update(request, id=None):

    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Updated Post!!!", extra_tags="bg-success")
        return redirect('posts:index')
    elif request.method == 'POST':
        messages.success(request, "Error: No Post Updated!!!", extra_tags="bg-danger")

    context = {
        'title': 'Edit Post',
        'instance': instance,
        'form': form,
    }
    return render(request, 'posts/post_form.html', context)


def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Successfully Deleted Post!!!", extra_tags="bg-success")
    return redirect('posts:index')
