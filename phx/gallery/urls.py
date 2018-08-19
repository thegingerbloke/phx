from django.urls import path
from . import views


urlpatterns = [
    path('', views.GalleryListView.as_view(), name='gallery-list'),
    path(
        '<int:pk>/<slug>/',
        views.GalleryDetailView.as_view(),
        name='gallery-detail'
    ),
]
