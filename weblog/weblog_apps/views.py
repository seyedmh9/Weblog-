from django.shortcuts import render

# Create your views here.

from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User , Categories ,Blog_Post_Management , Comment
from .serializers import UserSerializer , PostSerializer ,commentSerializer , CategoriesSerializer

# Create your views here.

# default views --------
@api_view(['GET','POST'])
def default(request):
    return Response('Ok')





#user views ----------------------------------------------

@api_view(['GET','POST'])
def user_list(request):
    if request.method == 'GET':
        users_query = User.objects.all()
        serializer = UserSerializer(users_query, many= True)
        t_count = users_query.count()
        content_range = f'0-{len(serializer.data)-1}/{t_count}'
        response = Response(serializer.data)
        response['Content-Range'] = content_range
        return response
    
    elif request.method == 'POST':
        new_user = UserSerializer(data = request.data)
        if new_user.is_valid():
            new_user.save()
            return Response(new_user.data,status=status.HTTP_201_CREATED)
        else:
            return Response(new_user.errors)


@api_view(['GET','DELETE','PUT'])
def user(request,id):
    if request.method == 'GET':
        user = get_object_or_404(User,pk=id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        dl_user = User.objects.get(pk = id)
        dl_user.delete()
        return Response('Ok')
    
    elif request.method == 'PUT':
        update = User.objects.get(pk = id)
        serializer = UserSerializer(update , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
# category views ----------------------------------------------

@api_view(['GET' , 'POST'])
def Categories_list(request):
    if request.method == 'GET':
        category_query = Categories.objects.all()
        serializer = CategoriesSerializer(category_query , many=True)
        t_count = category_query.count()
        content_range = f'0-{len(serializer.data)-1}/{t_count}'
        response = Response(serializer.data)
        response['Content-Range'] = content_range
        return response
    if request.method == 'POST':
        serializer = CategoriesSerializer (data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET' , 'PUT' , 'DELETE'])
def category(request , id):
    if request.method == 'GET':
        category = get_object_or_404(Categories , pk = id)
        serializer = CategoriesSerializer(category)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        update_category = Categories.objects.get(pk = id)
        serializer = CategoriesSerializer(update_category , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    elif request.method == 'DELETE':
        delete_category = Categories.objects.get(pk = id)
        delete_category.delete()
        return Response('Ok')
    


# Post view ---------------------------------------------

@api_view(['GET' , 'POST'])
def Post_list(request):
    if request.method == 'GET':
        query_post = Blog_Post_Management.objects.filter(status = 1)
        serializer = PostSerializer(query_post , many=True)
        t_count = query_post.count()
        content_range = f'0-{len(serializer.data)-1}/{t_count}'
        response = Response(serializer.data)
        response['Content-Range'] = content_range
        return response
    if request.method == 'POST':
        serializer = PostSerializer (data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET' , 'PUT' , 'DELETE'])
def Post(request , id):
    if request.method == 'GET':
        Post_query = get_object_or_404(Blog_Post_Management , pk = id)
        serializer = PostSerializer(Post_query)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        update_post = Blog_Post_Management.objects.get(pk = id)
        serializer = PostSerializer(update_post , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    if request.method == 'DELETE':
        delete_post = Blog_Post_Management.objects.get(pk = id)
        delete_post.delete()
        return Response('Ok')
    

# comment view --------------------------------------

@api_view(['GET' , 'POST'])
def comment_list(request):
    if request.method == 'GET':
        query_comment = Comment.objects.all()
        serializer = commentSerializer(query_comment , many=True)
        t_count = query_comment.count()
        content_range = f'0-{len(serializer.data)-1}/{t_count}'
        response = Response(serializer.data)
        response['Content-Range'] = content_range
        return response
    
    if request.method == 'POST':
        serializer = commentSerializer (data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET' , 'PUT' , 'DELETE'])

def comment(request , id):
    if request.method == 'GET':
        comment = get_object_or_404(Comment , pk = id)
        serializer = commentSerializer(comment)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        update_com = Comment.objects.get(pk = id)
        serializer = commentSerializer(update_com , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    if request.method == 'DELETE':
        delete = Comment.objects.get(pk = id)
        delete.delete()
        return Response('Ok')
    

# login view -----------------------------------------------------

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    try:
        check = User.objects.get(username=username, password=password)
        return Response("Ok", status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response("No", status=status.HTTP_404_NOT_FOUND)



    