from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics

from .serializers import PostSerializer
from .models import Post

class PublicPostListViewSet(generics.ListAPIView):
	queryset = Post.objects.filter(is_public=True)
	serializer_class = PostSerializer

class PostViewSet(ModelViewSet):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

	# Client에서 보내는 reqeust의 인코딩에 따라서 구성이 달라지는 것을 확인할 수 있는 dispatch 메소드 오버라이딩
#	def dispatch(self, request, *args, **kwargs):
#		print("reqeust.body : ", request.body)
#		print("reqeust.POST : ", request.POST)
#		return super().dispatch(request, *args, **kwargs)
