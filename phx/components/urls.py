from django.urls import path

from . import views

urlpatterns = [
    path('', views.ComponentsListView.as_view(), name='components-list'),
    path('<slug:group>/<slug:component>/',
         views.ComponentsDetailView.as_view(),
         name='components-detail'),
]
