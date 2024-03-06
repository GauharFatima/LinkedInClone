from django.urls import path
from . import views

urlpatterns = [
    # Set the feed view as the index view of the FeedApp
    path('', views.feed_view, name='feed'),
]
