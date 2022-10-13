from django.shortcuts import render,HttpResponseRedirect, redirect
from django.views.generic import TemplateView, CreateView
from .forms import NewUserForm, EditProfile
from django.contrib.auth.forms import AuthenticationForm
from .models import UserProfile
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from posts_app.models import Post
from posts_app.forms import PostForm
# Create your views here.

def sign_up(request):
    form = NewUserForm()
    registered = False
    if request.method == 'POST':
        form = NewUserForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            registered = True
            user_profile = UserProfile(user=user)
            user_profile.save()
            return HttpResponseRedirect(reverse('login_app:login'))
    diction = {'form':form, 'title':'Sign Up'}
    return render(request, 'login_app/signup.html', context=diction)


def log_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('posts_app:home'))
    diction = {'title':'Log in','form':form}
    return render(request, 'login_app/login.html', context=diction )

@login_required
def Edit_profile(request):
    current_user = UserProfile.objects.get(user= request.user)
    form = EditProfile()
    form = EditProfile(instance=current_user)
    if request.POST== 'POST':
        form = EditProfile(request.POST,request.FILES, instance=current_user)
        if form.is_valid():
            form.save()
            form = EditProfile(instance=current_user)
            return HttpResponseRedirect(reverse('login_app:user'))
    diction= {'form':form}
    return render(request, 'login_app/profile.html', context=diction)


@login_required
def logout_user(request):
    logout(request)
    return redirect('login_app:login')
@login_required
def user(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.author= request.user
            post.save()
            return redirect('posts_app:home')
    diction = {'form':form, 'title':'post'}
    return render(request, 'login_app/user.html', context= diction)

