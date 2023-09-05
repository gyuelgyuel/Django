from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('-id')
    comment_form = CommentForm()
    context = {
        'posts': posts,
        'comment_form': comment_form,
    }

    return render(request, 'index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:index')
    else:
        form = PostForm()

    context = {
        'form': form,
    }

    return render(request, 'posts/form.html', context)

@login_required
def comment_create(request, post_id):
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        post = Post.objects.get(id=post_id)
        comment.post = post
        comment.user = request.user
        comment.save()
        return redirect('posts:index')
        

@login_required
def like(request, id):
    user = request.user
    post = Post.objects.get(id=id)
    if post in user.like_posts.all():
        post.like_users.remove(request.user)
    
    else:
        post.like_users.add(request.user)
        
    return redirect('posts:index')