from django.urls import path

from posts import views

urlpatterns = [
    path('', views.IndexPage.as_view() , name="index"),
]