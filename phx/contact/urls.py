from django.urls import path

from . import views

urlpatterns = [
    path('', views.ContactIndexView.as_view(), name='contact-index'),
    path(
        'success/', views.ContactSuccessView.as_view(),
        name='contact-success'),
]
