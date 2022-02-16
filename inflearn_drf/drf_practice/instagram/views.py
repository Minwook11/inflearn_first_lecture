from django.shortcuts import render

from rest_framework.decorators import api_view

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics

from .serializers import PostSerializer
from .models import Post

#class PublicPostListView(generics.ListAPIView):
#	queryset = Post.objects.filter(is_public=True)
#	serializer_class = PostSerializer

	# CBV 형태로 DRF의 Views 만들기 -- APIView 상속
#class PublicPostListView(APIView):
#	def get(self, request):
#		qs = Post.objects.filter(is_public=True)
#		serializer = PostSerializer(qs, many=True)
#
#		return Response(serializer.data)
#
#public_post_list = PublicPostListView.as_view()

	# FBV 형태로 DRF의 Views 만들기 -- api_view() 데코레이터 사용
@api_view(['GET'])
def public_post_list(request):
	if request.method == 'GET':
		qs = Post.objects.filter(is_public=True)
		serializer = PostSerializer(qs, many=True)

		return Response(serializer.data)

class PostViewSet(ModelViewSet):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

	# Client에서 보내는 reqeust의 인코딩에 따라서 구성이 달라지는 것을 확인할 수 있는 dispatch 메소드 오버라이딩
#	def dispatch(self, request, *args, **kwargs):
#		print("reqeust.body : ", request.body)
#		print("reqeust.POST : ", request.POST)
#		return super().dispatch(request, *args, **kwargs)
