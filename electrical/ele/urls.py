from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from .views import signup, AddPostView, CustomLoginView, alumni_profile, faculty_profile
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
   
    path('acedemics/', views.acedemics, name='acedemics'),
    path('up/', views.up, name='up'),
    path("post/",views.post, name = "post"),
    path("Articles/", views.Articles, name = "Articles"),
    path('signup/', signup, name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('alumni/<str:username>/', alumni_profile, name='alumni_profile'),
    path('faculty/<str:username>/', faculty_profile, name='faculty_profile'),
    path('pfs/', views.pflist, name='pflist'),
    path('alumnies/', views.allist, name='allist'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    
]