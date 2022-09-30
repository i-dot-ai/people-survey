from django.contrib import admin
from django.urls import include, path

from people_survey.survey import views

urlpatterns = [
    path("", views.index_view, name="index"),
    path("questions/", views.questions_view, name="questions"),
    path("questions/<int:page_num>/", views.questions_view, name="questions"),
    path("finished/", views.finished_view, name="finished"),
    path("home/", views.homepage_view, name="homepage"),
    path("builder/", views.builder_view, name="builder"),
    path("survey/", views.survey_view, name="survey"),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
]
