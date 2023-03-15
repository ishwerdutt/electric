from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from ckeditor.fields import RichTextField
from django.urls import reverse


class CustomUser(AbstractUser):
    is_alumni = models.BooleanField(default=False)
    is_faculty = models.BooleanField(default=False)
    username = models.CharField(max_length = 20, unique = True, null=True)
    bio = models.TextField()
    company = models.TextField(null = True)
    subjects = models.CharField(max_length=50)
    profile_image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return str(self.username)
    def get_absolute_url(self):
        if self.is_alumni:
            return reverse('alumni_profile', args=[str(self.username)])
        elif self.is_faculty:
            return reverse('faculty_profile', args=[str(self.username)])
        else:
            return reverse('')
    
    
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=10,null = True)
    content = RichTextField(blank=True, null=True )
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    author_role = models.CharField(max_length=20, choices=[('alumni', 'Alumni'), ('faculty', 'Faculty')],null=True)
    document = models.FileField(upload_to='documents/', null=True, blank=True)
    
    
    def __str__(self):
        return str(self.title) or ''
    
    def get_absolute_url(self):
        return reverse("post")
# Create your models here.

# Create your models here.
