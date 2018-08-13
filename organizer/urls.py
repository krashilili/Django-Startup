from django.urls import path
from .views import tag_list, tag_detail, startup_list, startup_detail, TagCreate


urlpatterns = [
    path('tag/', tag_list, name='organizer_tag_list'),
    path('tag/create', TagCreate.as_view(),


         name='organizer_tag_create'),
    path('tag/<str:slug>', tag_detail, name='organizer_tag_detail'),
    path('', startup_list, name='organizer_startup_list'),
    path('startup/<str:slug>', startup_detail, name='organizer_startup_detail'),
]
