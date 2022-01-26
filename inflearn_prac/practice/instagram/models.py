from django.db import models

class Post(models.Model):
	message = models.TextField()
	is_public = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	# JAVA의 toString과 같은 역할의 함수
	def __str__(self):
		return f'Custom Post Object ({self.id})'

	# Method는 Admin 에서도 선언하여 사용 가능하다. 목적이나 빈도에 따라서 Models에 선언할 지, Admin에 선언할 지 선택하여 사용
	def message_length(self):
		return len(self.message)
	message_length.short_description = "메세지 글자수" # Admin 페이지에서의 Row 이름 지정, Default는 함수 이름
