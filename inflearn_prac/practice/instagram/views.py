from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator

from .models import Post

# Django에서 기본 제공하는 ListView, 아래 Views와 차이점은 검색 안됨
# paginate_by 옵션을 통해서 기본 지원되는 페이징 기능 실습
# FBV에 데코레이터 적용하기 -- login_decorator
#post_list = login_decorator(ListView.as_view(model = Post, paginate_by=10))

# Class에 직접 데코레이터를 적용하는 방식 -- @키워드를 사용하거나, 해당되는 Mixin을 상속 시키는 방식이 있다.
#@method_decorator(login_required, name='dispatch')
class PostListView(LoginRequiredMixin, ListView):
	model = Post
	paginate_by = 10

post_list = PostListView.as_view()

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

class PostDetailView(DetailView):
	model = Post
#	qs = Post.objects.filter(is_public = True)

#	get_queryset 오버라이딩 진행 - 로그인 한 사용자의 public란 포스팅에 대한 데이터 획득 로직
	def get_queryset(self):
		qs = super().get_queryset()
		if not self.request.user.is_authenticated:
			qs = qs.filter(is_public=True)
		return qs

post_detail = PostDetailView.as_view(model=Post, pk_url_kwarg='id')

def archives_year(request, year):
	response = HttpResponse()
	response.write('{} Year Archives'.format(year))

	return response
