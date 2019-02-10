from django.urls import path

from . import views

urlpatterns = [
    path('', views.FixturesListView.as_view(), name='fixtures-index'),
]
