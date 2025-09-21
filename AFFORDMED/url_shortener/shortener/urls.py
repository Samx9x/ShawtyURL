from django.urls import path
from . import views

urlpatterns = [
    path("shorturls", views.create_shorturl),
    path("shorturls/<str:shortcode>", views.stats_shorturl),
    path("<str:shortcode>", views.redirect_shorturl),
]
