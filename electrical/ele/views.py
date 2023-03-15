# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post, CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm, PostForm
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, CreateView
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'ele/index.html')

def acedemics(request):
    return render(request, 'ele/acedemics.html')


def up(request):
    return render(request, 'ele/up.html')


def Articles(request):
    faculty_posts = Post.objects.filter(author_role='faculty')
    print(faculty_posts)

    context = {'faculty_posts': faculty_posts}
    return render(request, 'ele/articles.html', context)



def post(request):
    alumni_posts = Post.objects.filter(author_role='alumni')
    print(alumni_posts)
    

    context = {'alumni_posts': alumni_posts}
    return render(request, 'ele/alumni_post.html', context)





#def signup(request, role):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            if role == 'alumni':
                CustomUser.objects.create()
            elif role == 'faculty':
                CustomUser.objects.create()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'ele/signup.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'ele/signup.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'ele/loginpage.html'

    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_alumni:
                return reverse('alumni_profile', kwargs={'username': user.username})
            elif user.is_faculty:
                return reverse('faculty_profile', kwargs={'username': user.username})
        return '/'

@login_required
def alumni_profile(request, username):
    user = get_object_or_404(CustomUser, username=username, is_alumni=True)
    posts = Post.objects.filter(author=user)
    return render(request, 'ele/profile.html', {'user': user, 'posts': posts})

@login_required
def faculty_profile(request, username):
    user = get_object_or_404(CustomUser, username=username, is_faculty=True)
    posts = Post.objects.filter(author=user)
    return render(request, 'ele/pf_profile.html', {'user': user, 'posts': posts})



#def get_user_profile(request, username):
    user = CustomUser.objects.get(username=username)
    user_posts = Post.objects.filter(author=user)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = user
            post.save()
            return redirect('profile')
    else:
        form = PostForm()
    context = {
        'user': user,
        'alumni_posts': user_posts,
        'form': form
    }
    return render(request, 'ele/profile.html', context)


#def get_pf_profile(request, username):
    pf1 = CustomUser.objects.get(username=username, is_faculty=True)
    if not pf1.is_faculty:
        return redirect('login')
    pf_posts = Post.objects.filter(author=pf1)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            pf_posts = form.save(commit=False)
            pf_posts.author = pf1
            pf_posts.save()
            return redirect('pf_profile')
    else:
        form = PostForm()
    context = {
        'pf1': pf1,
        'pf_posts': pf_posts,
        'form': form
    }
    return render(request, 'ele/pf_profile.html', context)






def pflist(request):
    pfs = CustomUser.objects.filter(is_faculty=True)
    context = {
        'pfs': pfs,

    }
    return render(request, 'ele/pf.html', context)


def allist(request):
    alumnies = CustomUser.objects.filter(is_alumni=True)
    context = {
        'alumnies': alumnies,

    }
    return render(request, 'ele/alumnies.html', context)



class AddPostView(CreateView):
    model = Post
    template_name = 'ele/add_post.html'
    fields = '__all__'


