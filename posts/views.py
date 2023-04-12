from django.db import IntegrityError
from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from .forms import CustomLoginForm, CustomUserCreationForm, PostForm, CommentForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db.models import Q, F
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import F
# Create your views here.

banned_list = ['pig', 'hohol']


def login_user(request):
    form = CustomLoginForm()
    if request.method=='GET':
        return render(request, 'posts/login.html', context={'form':form})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('start_page')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
            return render(request, 'posts/login.html', {'form':form})



def signup_user(request):
    form = CustomUserCreationForm()
    if request.method == 'GET':
        return render(request, 'posts/signup.html', context={'form':form})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                new_user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                new_user.save()
                login(request, new_user)
                return redirect('start_page')
            except IntegrityError:
                messages.error(request, 'User with such username already exists. Please choose another nickname.')
                return render(request, 'posts/signup.html', context={'form':form})
        else:
            messages.error(request, 'You should enter the exact same password twice. Please repeat once more.')
            return render(request, 'posts/signup.html', context={'form':form})


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('start_page')

def start_page(request):
    posts = PostsModel.objects.all()
    paginator = Paginator(posts, 3)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_num)
    return render(request, 'posts/home_page.html', context={'posts': posts, 'page_obj':page_obj})


def show_by_category(request, cattitle):
    posts = PostsModel.objects.filter(category__title=cattitle).select_related()
    paginator = Paginator(posts, 3)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_num)
    return render(request, 'posts/show_by_category.html', context={'posts':posts, 'page_obj':page_obj})


def add_post(request):
    if request.method == 'GET':
        form = PostForm()
        return render(request, 'posts/add_post.html', context={'form':form})
    else:
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            if any(word in form.cleaned_data['title'] for word in banned_list):
                post = PostsModel.objects.create(title=form.cleaned_data['title'], content=form.cleaned_data['content'], category=form.cleaned_data['category'], user=request.user, published=False)
            else:
                post = PostsModel.objects.create(**form.cleaned_data, user=request.user)
                post.save()
                return redirect('start_page')
        else:
            messages.error(request, 'Sorry, there was an error while creating the post. Please try again.')
            return render(request, 'posts/add_post.html', context={'form':form})


def show_detail(request, title):
    post = get_object_or_404(PostsModel, title=title)
    post.views = F('views') + 1
    post.save()
    form = CommentForm()
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comm = Comments.objects.create(content=form.cleaned_data['content'], user=request.user, post=post)
            comm.save()
            return render(request, 'posts/detailed_post.html', context={'form':form,'post':post})
    else:
        return render(request, 'posts/detailed_post.html', context={'form':form,'post':post})


# def show_detail(request, title):
#     post = get_object_or_404(PostsModel, title=title)
#     return render(request, 'posts/detailed_post.html', context={'post':post})


# def create_comment(request, title):
#     form = CommentForm()
#     post = PostsModel.objects.get(title=title)
#     if request.method=='POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comm = Comments.objects.create(content=form.cleaned_data['content'], user=request.user, post=post)
#             comm.save()
#             return render(request, 'posts/detailed_post.html', context={'form':form,'post':post})
#     else:
#         return render(request, 'posts/detailed_post.html', context={'form':form,'post':post})