from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("a", views.index, name="index"),
    path("<int:pk>", views.announcement_detail, name="announcement_detail"),
    path("gallery/<int:pk>/", views.gallery, name="gallery"),
    path("upload/", views.upload, name="upload"),
    path("photos/<int:pk>/", views.delete_photo, name="delete_photo"),
    path("profile/<int:pk>", views.profile, name="profile" ),
    path("profile/update_profile", views.update_profile, name="update_profile"),
    path("search_announcements", views.search_announcements, name="search_announcements"),
    path("about", views.about, name="about"),
    path("create_company", views.create_company, name="create_company"),
    path("company_profile/edit_company", views.edit_company, name="edit_company"),
    path("search_jobs/edit_job/<int:pk>", views.edit_job, name="edit_job"),
    path("search_jobs/delete_job/<int:pk>", views.delete_job, name="delete_job"),
    path("company/<int:pk>", views.company, name="company"),
    path("company_profile/<int:pk>", views.company_profile, name="company_profile"),
    path("companies", views.companies, name="companies"),
    path("company_profile/add_job", views.add_job, name="add_job"),
    path("search_jobs", views.search_jobs, name="search_jobs"),
    path("search_jobs/<int:pk>", views.job_offer, name="job_offer"),
]
