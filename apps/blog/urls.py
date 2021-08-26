from django.urls import path

from apps.blog.views import CategoryViewSet, BlogListView, BlogItemView,BlogViewSet,CommentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'blogs', BlogViewSet, basename='blogs')
router.register(r'comments', CommentViewSet, basename='comments')

urlpatterns = router.urls

urlpatterns += [
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/comment/<int:pk>/', BlogItemView.as_view(), name='blog_item'),
]
