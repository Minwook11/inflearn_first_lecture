from django.urls import path, re_path, register_converter

from . import views
from .converters import YearConverter, MonthConverter, DayConverter

# Custom Path Converter 등록
register_converter(YearConverter, 'year')
register_converter(MonthConverter, 'month')
register_converter(DayConverter, 'day')

app_name = 'instagram'

urlpatterns = [
	path('new/', views.post_new, name='post_new'),
#	Reverse Name 지정 후 RedirectView를 통해서 테스트 진행
	path('', views.post_list, name='post_list'),
	path('<int:id>/', views.post_detail, name='post_detail'),
#	re_path(r'(?P<id>\d+)/$', views.post_detail),	# 정규 표현식 사용례, 위와 동일하게 작동
#	path('archives/<int:year>/', views.archives_year),
#	re_path(r'archives/(?P<year>\d+)/', views.archives_year),
#	path('archives/<year:year>/', views.archives_year),	# Custom Path Converter 적용
	path('archive/', views.post_archive, name='post_archive'),
	path('archive/<year:year>/', views.post_archive_year, name='post_archive_year'),
#	path('archive/<year:year>/<month:month>/', views.post_archive_month, name='post_archive_month'),
#	path('archive/<year:year>/<month:month>/<day:day>/', views.post_archive_day, name=Post_archive_day),
]
