from . import views
from django.urls import path

urlpatterns = [
    path("bg_index/", views.PostList.as_view(), name="blog_index"),
    path("<slug:slug>/", views.PostDetail.as_view(), name="post_detail"),
]
