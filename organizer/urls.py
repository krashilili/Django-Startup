from django.urls import path
from .views import homepage, tag_detail, startup_list

urlpatterns = [
    path('', homepage),
    path('tag/<str:slug>', tag_detail),
    path('startup/', startup_list),
]
