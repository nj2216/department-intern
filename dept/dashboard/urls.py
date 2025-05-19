from django.urls import path
from . import views

urlpatterns = [
    path("", views.hom, name="home"),
    path("edit/<int:dept_id>/", views.edit, name="edit"),
]