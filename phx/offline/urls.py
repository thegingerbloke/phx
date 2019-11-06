from django.urls import path

from . import views

urlpatterns = [
    path('', views.OfflineView.as_view(), name='offline-index'),
]
