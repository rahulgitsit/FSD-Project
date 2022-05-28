from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("land", views.index, name="land"),
    # path("index/", views.index, name="index"),
    path("forms/", views.get_degree, name="forms"),
    path("student/", views.get_student, name="student"),
]
