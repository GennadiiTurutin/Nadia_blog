from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (
	PostListView, 
	PostDetailView,
	PostCreateView,
	PostUpdateView,
	PostDeleteView, 
    search
	)

from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-art_design'),
    path('Inspiration/', views.inspiration, name='blog-inspiration'), 
    path('Lifestyle/', views.lifestyle, name='blog-lifestyle'),
    path('About/', views.about, name='blog-about'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), 
    path('results/$', search, name='search')
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)