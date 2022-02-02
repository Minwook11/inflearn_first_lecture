from django.urls import path, re_path

from .import views

urlpatterns = [
	path('', views.post_list),
	path('<int:id>/', views.post_detail),
#	re_path(r'(?P<id>\d+)/$', views.post_detail),	# 정규 표현식 사용례, 위와 동일하게 작동
]
