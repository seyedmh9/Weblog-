from rest_framework import serializers
from .models import User , Blog_Post_Management , Categories , Comment
from django.conf import settings

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'profile_picture']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request')
        if instance.profile_picture:
            if request is not None:
                host = request.get_host()
                representation['profile_picture'] = request.build_absolute_uri(instance.profile_picture.url)
            else:
                representation['profile_picture'] = f"{settings.DEFAULT_HOST}{instance.profile_picture.url}"
        return representation
    
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog_Post_Management
        fields = ['id', 'user_id', 'title', 'Description', 'category_id', 'tag', 'image', 'status']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request')
        if instance.image:
            if request is not None:
                host = request.get_host()
                representation['image'] = request.build_absolute_uri(instance.image.url)
            else:
                representation['image'] = f"{settings.DEFAULT_HOST}{instance.image.url}"
        return representation


class commentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','user_id', 'post_id', 'Description']

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id','name', 'created_at', 'Description']