from django.urls import path
from . import views


app_name = 'core'


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<slug:post>/', views.post_detail, name='post_detail'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag')
]
