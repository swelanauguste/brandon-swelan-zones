from django.contrib import admin
from django.urls import path
from zones import views

urlpatterns = [
    path("", views.ZoneListView.as_view(), name="list"),
    path("<slug:slug>/", views.ZoneDetailView.as_view(), name="detail"),
    path("admin/", admin.site.urls),
]
