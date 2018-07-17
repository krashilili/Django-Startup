from django.urls import path
from .views import post_list, post_detail

urlpatterns = [
    path('', post_list),
    path('post/<int:year>/<int:month>/<str:slug>', post_detail),
]