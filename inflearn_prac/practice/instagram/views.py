from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Post

post_list = ListView.as_view(model = Post)	# Django에서 기본 제공하는 ListView, 아래 Views와 차이점은 검색이 안됨

#def post_list(request):
#	query_set = Post.objects.all()
#	q = request.GET.get('q', '')	# 입력받은 검색 조건이 있으면 q에 저장 없으면 ''
#	if q:
#		query_set = query_set.filter(message__icontains = q)	# 검색어가 포함된 Queryset만 필터링
#	return render(request, 'instagram/post_list.html', {
#		'post_list' : query_set,	# 결과 Queryset 전달
#		'q' : q						# 입력받은 검색 조건 전달
#	})

# Views의 인자 중 URL에서 읽어오는 인자를 URL Captured Values라고 말함
#def post_detail(request: HttpResponse, id: int) -> HttpResponse:
#	post = get_object_or_404(Post, id = id)
#	return render(request, 'instagram/post_detail.html', {
#			'post' : post,
#		})
post_detail = DetailView.as_view(model=Post, pk_url_kwarg='id')

def archives_year(request, year):
	response = HttpResponse()
	response.write('{} Year Archives'.format(year))

	return response
