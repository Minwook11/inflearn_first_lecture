from django.urls import path, re_path, register_converter

from .import views

# Custom Path Converter 선언
class YearConverter:
	regex = '20\d{2}'	# 2000년대에 해당되는 숫자 처리

	def to_python(self, value):
		return int(value)
	
	def to_url(self, value):
		return str(value)

# Custom Path Converter 등록
register_converter(YearConverter, 'year')

app_name = 'instagram'

urlpatterns = [
	path('', views.post_list),
	path('<int:id>/', views.post_detail),
#	re_path(r'(?P<id>\d+)/$', views.post_detail),	# 정규 표현식 사용례, 위와 동일하게 작동
#	path('archives/<int:year>/', views.archives_year),
#	re_path(r'archives/(?P<year>\d+)/', views.archives_year),
	path('archives/<year:year>/', views.archives_year),	# Custom Path Converter 적용
]
