from rest_framework import serializers, status
from .models import Projects, Blog, userfeedback, SocialLinks, About, Skills
from rest_framework.response import Response
class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = "title", "image", "content", "link", "created_at", "updated_at","id"
    
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "title","id", "image", "content", "created_at", "updated_at","description"
class userfeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = userfeedback
        fields = "name", "message", "created_at", "updated_at","id"
class SocialLinksSerializer(serializers.ModelSerializer):  
    class Meta:
        model = SocialLinks
        fields = "Linkdn", "Github", "Instagram", "Facebook","id"
    
class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = "image", "content", "created_at", "updated_at","id","document"

    def create(self, validated_data):
      if About.objects.exists():
        Response({"message": "About already exists"}, status=status.HTTP_400_BAD_REQUEST)
      return About.objects.create(**validated_data)
class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = "title", "image", "content", "created_at", "updated_at"