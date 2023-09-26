from django.db import models
from ckeditor.fields import RichTextField

class Blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    content = RichTextField(blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class userfeedback(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Projects(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    content = models.TextField()
    link = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class SocialLinks(models.Model):
    Linkdn=models.CharField(max_length=100,null=True,blank=True)
    Github=models.CharField(max_length=100,null=True,blank=True)
    Instagram=models.CharField(max_length=100,null=True,blank=True)
    Facebook=models.CharField(max_length=100,null=True,blank=True)
class About(models.Model):
    image = models.ImageField(upload_to='images/')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    document=models.FileField(upload_to='documents/',null=True,blank=True)
class Skills(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

