"""
URL configuration for portfoliobackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mainapp.views import ProjectsViewSet, BlogViewSet, userfeedbackViewSet, SocialLinksViewSet, AboutViewSet, SkillsViewSet
from django.conf import settings
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.urls import include
router = DefaultRouter()
router.register('projects', ProjectsViewSet, basename='projects')
router.register('blog', BlogViewSet, basename='blog')
router.register('userfeedback', userfeedbackViewSet, basename='userfeedback')
router.register('sociallinks', SocialLinksViewSet, basename='sociallinks')
router.register('about', AboutViewSet, basename='about')
router.register('skills', SkillsViewSet, basename='skills')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
