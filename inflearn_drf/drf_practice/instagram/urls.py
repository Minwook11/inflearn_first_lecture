from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('post', views.PostViewSet)

urlpatterns = [
	path('public/', views.PublicPostListViewSet.as_view()),
	path('', include(router.urls)),
]
