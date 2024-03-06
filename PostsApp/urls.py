from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    # function base view
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('create/', views.post_create, name='post_create'),
    path('update/<int:pk>/', views.post_update, name='post_update'),
    path('delete/<int:pk>/', views.post_delete, name='post_delete'),
    path('<int:pk>/like/', views.toggle_like, name='toggle_like'),
    path('<int:pk>/submit_comment/', views.submit_comment, name='submit_comment'),
    path('<int:pk>/get_comments/', views.get_comments, name='get_comments'),


    # class base view
    # path('', views.PostListView.as_view(), name='post_list'),
    # path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    # path('create/', views.post_create, name='post_create'),
    # path('update/<int:pk>/', views.PostUpdateView.as_view(), name='post_update'),
    # path('delete/<int:pk>/', views.PostDeleteView.as_view(), name='post_delete'),
]
