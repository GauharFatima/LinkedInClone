from django.urls import path
from AccountsApp import views

urlpatterns = [
    path('signup/', views.createUser, name='signup'),
    path('login/', views.existingUser, name='login'),
    # path('feeds/', views.feedsView, name='feeds'),
    path('logout/', views.logoutUser, name='logout')
]