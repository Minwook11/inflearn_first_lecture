from django.shortcuts import render

from rest_framework.decorators import api_view, action

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework.generics import RetrieveAPIView
from rest_framework.renderers import TemplateHTMLRenderer

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


# ViewSet에 새로운 endpoint 추가하기
class PostViewSet(ModelViewSet):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

	# DOTO: Author관련하여 임시로 로그인이 되어 있다는 가정하에 진행됨
	def perform_create(self, serializer):
		author = self.request.user	# User or AnonymousUser 객체 둘 중 하나
		ip = self.request.META['REMOTE_ADDR']
		serializer.save(ip=ip, author=author)

	# detail값의 구분은 False라면 컬렉션/목록 요청, True라면 인스턴스/세부 정보 요청으로 구분됨
	@action(detail=False, methods=['GET'])
	def public(self, request):
		qs = self.queryset.filter(is_public=True)
		serializer = self.get_serializer(qs, many=True)

		return Response(serializer.data)

	@action(detail=True, methods=['PATCH'])
	def invert_public(self, request, pk):
		instance = self.get_object()
		if instance.is_public:
			instance.is_public=False
		else:
			instance.is_public=True

		instance.save()
		serializer = self.get_serializer(instance)

		return Response(serializer.data)

	# Client에서 보내는 reqeust의 인코딩에 따라서 구성이 달라지는 것을 확인할 수 있는 dispatch 메소드 오버라이딩
#	def dispatch(self, request, *args, **kwargs):
#		print("reqeust.body : ", request.body)
#		print("reqeust.POST : ", request.POST)
#		return super().dispatch(request, *args, **kwargs)

class PostDetailAPIView(RetrieveAPIView):
	queryset = Post.objects.all()
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'instagram/post_detail.html'

	def get(self, request, *args, **kwargs):
		post = self.get_object()
		return Response({
				'post' : post,
			})
