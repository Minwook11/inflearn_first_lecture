from django.shortcuts import render

from .models import Post

def post_list(request):
	query_set = Post.objects.all()
	q = request.GET.get('q', '')	# 입력받은 검색 조건이 있으면 q에 저장 없으면 ''
	if q:
		query_set = query_set.filter(message__icontains = q)	# 검색어가 포함된 Queryset만 필터링
	return render(request, 'instagram/post_list.html', {
		'post_list' : query_set,	# 결과 Queryset 전달
		'q' : q						# 입력받은 검색 조건 전달
	})
