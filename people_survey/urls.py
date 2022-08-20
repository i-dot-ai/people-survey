from django.urls import include, path
from django.contrib import admin

from people_survey.survey import views

urlpatterns = [
    path("", views.index_view, name="index"),
    path("home/", views.homepage_view, name="homepage"),
    path("admin/", admin.site.urls),
    path("api/", views.api.urls),
    path('accounts/', include('allauth.urls')),
]
