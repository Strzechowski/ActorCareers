from django.urls import path
from . import views

urlpatterns = [
    path("", views.announcement, name="announcement"),
    path("a", views.index, name="index"),
    path("<int:pk>", views.announcement_detail, name="announcement_detail"),
    path("photos/", views.photo_list, name='photo_list'),
    path("upload/", views.upload, name="upload"),
    path("photos/<int:pk>/", views.delete_photo, name="delete_photo"),
]
