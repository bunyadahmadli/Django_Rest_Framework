from django.urls import path, include
from .views import PostListAPIView , PostDetailAPIView, PostDeleteAPIView,PostUpdateAPIView,PostCreateAPIView
from django.views.decorators.cache import cache_page
app_name ='post'
urlpatterns = [
    path('posts', cache_page(60*1)(PostListAPIView.as_view()), name='posts'),
    path('posts/detail/<slug>', PostDetailAPIView.as_view(), name='detail'),
    path('posts/delete/<slug>', PostDeleteAPIView.as_view(), name='delete'),
    path('posts/update/<slug>', PostUpdateAPIView.as_view(), name='update'),
    path('posts/create/', PostCreateAPIView.as_view(), name='create'),
]
