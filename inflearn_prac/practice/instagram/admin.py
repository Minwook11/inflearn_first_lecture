from django.contrib import admin

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	# Admin 페이지에서 보여줄 Models 객체들의 데이터 지정
	# Models 클래스에 정의된 Method도 지정할 수 있다. ex) --> message_length
	list_display = ['id', 'message', 'is_public', 'message_length', 'created_at', 'updated_at']
	list_display_links = ['id', 'message'] # Admin 페이지에서 링크 활성화 할 Row 지정
	# Admin에서 제공하는 검색 UI를 활용하여, 검색할 수 있는 대상을 지정
	search_fields = ['message']
	# Admin에서 제공하는 필터 UI를 활ㅇ용하여, 필터링의 기준이 될 대상을 지정
	list_filter = ['created_at', 'is_public']

	# Method는 Admin 에서도 선언하여 사용 가능하다. 목적이나 빈도에 따라서 Models에 선언할 지, Admin에 선언할 지 선택하여 사용
#	def message_length(self, post):
#		return len(post.message)
