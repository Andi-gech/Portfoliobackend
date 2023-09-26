from django.shortcuts import render
from rest_framework import viewsets
from .models import Projects, Blog, userfeedback, SocialLinks, About, Skills
from .Serializers import ProjectsSerializer, BlogSerializer, userfeedbackSerializer, SocialLinksSerializer, AboutSerializer, SkillsSerializer
from django.http import HttpResponse

from rest_framework.response import Response


class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all().order_by('-created_at')
    serializer_class = ProjectsSerializer  
  
class BlogViewSet(viewsets.ModelViewSet):    
    queryset = Blog.objects.all().order_by('-created_at')
    serializer_class = BlogSerializer   
class userfeedbackViewSet(viewsets.ModelViewSet):    
    queryset = userfeedback.objects.all()
    serializer_class = userfeedbackSerializer
class SocialLinksViewSet(viewsets.ModelViewSet):
    queryset = SocialLinks.objects.all()
    serializer_class = SocialLinksSerializer
class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
class SkillsViewSet(viewsets.ModelViewSet):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer
