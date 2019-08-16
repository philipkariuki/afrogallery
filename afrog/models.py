from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length =260)    
    pub_date = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(default=0, max_length =14)
    pic = models.ImageField(upload_to = 'profilepics2/', blank=True )

    def __str__(self):
        return self.user.username



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()



class Project(models.Model):
    title = models.CharField(max_length =60)
    description = models.CharField(max_length =600)
    link = models.URLField(max_length =60)
    pub_date = models.DateTimeField(auto_now_add=True)
    projimage = models.ImageField(upload_to = 'postimages/', blank=True )
    comments = models.ForeignKey
    poster = models.ForeignKey(UserProfile)  # change to poster /


    def __str__(self):
        return self.title
    
    
    @classmethod
    def get_projects(cls):
        projos = cls.objects.all()
        return projos


    @classmethod
    def search_by_title(cls,search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects


    def delete_project(self):
        self.delete()       

    def save_project(self):
        self.save()

    


class Comments(models.Model):
    comment_content = models.CharField(max_length = 200)
    project = models.ForeignKey(Project)
    profile = models.ForeignKey(UserProfile)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.comment_content

    def save_comment(self):
        self.save()