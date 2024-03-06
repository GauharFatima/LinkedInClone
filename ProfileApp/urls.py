from django.urls import path
from . import views


app_name = 'ProfileApp'

urlpatterns = [
    path('<int:user_id>/', views.profile_detail, name='profile_detail'),
    path('test/', views.profile_test, name='profile_test'),
    path('complete/', views.complete_profile, name='complete_profile'),

    # path('all/', views.complete_profile, name='complete_profile'),
]
