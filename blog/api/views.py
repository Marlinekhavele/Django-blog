from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from users.models import Profile

from blog.models import Post,Comment
from blog.api.serializers import PostSerializer


@api_view(['GET','POST'])
def posts_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializers = PostSerializer(posts,many=True)
        return Response(serializers.data)

    elif(request.method == 'POST'):
        serializers = PostSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','PUT','DELETE'])
def posts_details(request,pk):
    try:
        posts = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializers = PostSerializer(posts)
        return Response(serializers.data)

    elif request.method == 'PUT':
        serializers = PostSerializer(posts,request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        posts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)










