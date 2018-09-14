from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (
	PostListView, 
	PostDetailView,
	PostCreateView,
	PostUpdateView,
	PostDeleteView
	)

from . import views

urlpatterns = [
    path('', views.me, name='blog-me'),
    path('blog', PostListView.as_view(), name='blog-blog'),
    path('gallery/', views.gallery, name='blog-gallery'), 
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), 

    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)