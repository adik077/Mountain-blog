from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from tinymce.models import HTMLField

class Category(models.Model):
    category=models.CharField(max_length=60)

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return reverse('main')


class Profile(models.Model):
    user=models.OneToOneField(User,null=True,blank=True, on_delete=models.CASCADE)
    bio=models.TextField(null=True, blank=True)
    profile_pic=models.ImageField(null=True, blank=True, upload_to="images/profile_pic")
    facebook_url=models.CharField(max_length=200,null=True, blank=True)
    twitter_url=models.CharField(max_length=200,null=True, blank=True)
    instagram_url=models.CharField(max_length=200,null=True, blank=True)

    def __str__(self):
        return str(self.user)

class Post(models.Model):
    title=models.CharField(max_length=30, null=False, blank=False)
    creation_date=models.DateTimeField(auto_now=True)
    tag=models.CharField(max_length=60,null=False,blank=False)
    #body=models.TextField(null=False,blank=False)
    snippet=models.TextField(null=False,blank=False,default='Stworz krotki opis...',max_length=300)
    body=HTMLField(null=False,blank=False,default='Dodaj artykul...')
    category=models.CharField(max_length=60, default='gory')
    post_picture=models.ImageField(blank=True,null=True, upload_to="images/")
    post_picture_admin=models.ImageField(blank=True,null=True, upload_to="images/admin")
    is_active=models.NullBooleanField(default=True)
    is_highlited=models.NullBooleanField(default=False)
    like=models.ManyToManyField(User,related_name='blog_posts')
    author=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title+" | "+str(self.author)

    def get_absolute_url(self):
        return reverse('main')

    def total_likes(self):
        return self.like.count()

class Comments(models.Model):
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now=True)
    body=models.TextField(max_length=500)
    class Meta:
        ordering=['-date']

    def __str__(self):
        return str(self.post.title)+" Skomentowano przez: "+str(self.comment_author)


