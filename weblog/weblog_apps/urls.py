from django.urls import path
from . import views

urlpatterns = [
    path("",views.default),
    path("Users",views.user_list),
    path("Users/",views.user_list),
    path("Users/<id>",views.user),
    path("Users/<id>/",views.user),
    path('Categories/' , views.Categories_list),
    path('Categories' , views.Categories_list),
    path('Categories/<id>/' , views.category),
    path('Categories/<id>' , views.category),
    path('Posts/' , views.Post_list),
    path('Posts' , views.Post_list),
    path('Posts/<id>/' , views.Post),
    path('Posts/<id>' , views.Post),
    path('comments/' , views.comment_list),
    path('comments' , views.comment_list),
    path('comments/<id>/' , views.comment),
    path('comments/<id>' , views.comment),
    path('login/' , views.login),
]

