from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import User , Categories , Blog_Post_Management , Comment
# Register your models here.

admin.site.register(User)
admin.site.register(Categories)
admin.site.register(Blog_Post_Management)
admin.site.register(Comment)

