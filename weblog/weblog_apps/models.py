from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    profile_picture = models.ImageField(upload_to='profile_picture/')

class Categories(models.Model):
    name = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    Description = models.TextField()

class Blog_Post_Management(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    Description = models.TextField()
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    tag = models.CharField(max_length=50)
    image = models.ImageField(upload_to = 'image/')
    status = models.CharField(max_length=7)

    
class Comment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Blog_Post_Management,on_delete=models.CASCADE)
    Description = models.TextField()