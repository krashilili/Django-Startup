from django.urls import path
from .views import PostList, post_detail

urlpatterns = [
    path('',
         PostList.as_view(template_name='blog/post_list.html'),
         name='blog_post_list'),

    path('post/<int:year>/<int:month>/<str:slug>',
         post_detail,
         name='blog_post_detail'),
]