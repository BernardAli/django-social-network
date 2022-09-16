from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post-list'),
    path('<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('<int:pk>/update', views.PostUpdateView.as_view(), name='post-update'),
    path('<int:pk>/delete', views.PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/like', views.AddLike.as_view(), name='like'),
    path('post/<int:pk>/dislike', views.AddDislike.as_view(), name='dislike'),
    path('post/<int:post_pk>/comment/delete/<int:pk>', views.CommentDeleteView.as_view(), name='comment-delete'),
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>/', views.ProfileUpdateView.as_view(), name='profile-edit'),
    path('profile/<int:pk>/followers/add', views.AddFollower.as_view(), name='add-follower'),
    path('profile/<int:pk>/followers/remove', views.RemoveFollower.as_view(), name='remove-follower'),
    path('search/', views.UserSearch.as_view(), name='profile-search'),
]