from django.contrib import admin

# Register your models here.
from .models import Blog,userfeedback,Projects,SocialLinks,About,Skills

admin.site.register(Blog)
admin.site.register(userfeedback)
admin.site.register(Projects)
admin.site.register(SocialLinks)
admin.site.register(About)

admin.site.register(Skills)
admin.site.site_header = "Portfolio Admin"
admin.site.site_title = "Portfolio Admin Portal"
admin.site.index_title = "Welcome to Portfolio Researcher Portal"
