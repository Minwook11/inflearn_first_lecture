from django.conf import settings
from django.core.validators import MinLengthValidator
from django.db import models
from django.urls import reverse

class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	message = models.TextField(
			validators=[MinLengthValidator(10)]
	)
	# ImageField는 pillow 라이브러리 dependency 존재, upload_to 옵션을 통해서 settings의 MEDIA_ROOT와 조합하여 파일이 저장될 위치를 지정 가능함
	# upload_to에서 시간관련 키워드를 사용해서 원하는 시간 단위로 저장 파일을 구분할 수 있다.
	image = models.ImageField(blank=True, upload_to='instagram/image/%Y%m%d')
	tag_set = models.ManyToManyField('Tag', blank=True)	# 동작 및 목적에 따라 blank 옵션 True/False
	is_public = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	class Meta:
		ordering = ['-id']	# 기본 정렬 지정, ID의 역순 - 즉, 최신 글부터

	# URL Reverse 사용을 위한 Wrapper 메소드 구현
	def get_absolute_url(self):
		return reverse('instagram:post_detail', args=[self.pk])

	# JAVA의 toString과 같은 역할의 함수
	def __str__(self):
		return f'Custom Post Object ({self.id})'

	# Method는 Admin 에서도 선언하여 사용 가능하다. 목적이나 빈도에 따라서 Models에 선언할 지, Admin에 선언할 지 선택하여 사용
	def message_length(self):
		return len(self.message)
	message_length.short_description = "메세지 글자수" # Admin 페이지에서의 Row 이름 지정, Default는 함수 이름

class Comment(models.Model):
	# limit_choices_to 옵션을 사용해서 조건을 지정할 수 있음
	# related_name 옵션을 통해서 reverse_name을 지정할 수 있음, 기본은 소문자 모델 클래스 이름 + '_set'
	post = models.ForeignKey(Post, on_delete=models.CASCADE, 
			limit_choices_to={'is_public':True},	
			related_name='current_post_comment')
	message = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Tag(models.Model):
	name = models.CharField(max_length=50, unique=True)
#	post_set = ManyToManyField(Post)
