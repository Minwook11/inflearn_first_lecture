import re

from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['message', 'image', 'tag_set', 'is_public']

	# clean_필드명 메소드를 사용하는 예제
	def clean_message(self):
		message = self.cleaned_data.get('message')
		if message:
			message = re.sub(r'[a-zA-z]+', '', message)	#입력값의 변환 정규식 -- 영어만 기록
		return message
