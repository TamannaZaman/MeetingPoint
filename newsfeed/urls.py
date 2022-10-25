from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from .views import PostUpdateView, PostListView, UserPostListView

urlpatterns = [
    path('users/', views.users_list, name='users_list'),
    path('users/<slug>/', views.profile_view, name='profile_view'),
    path('friends/', views.friend_list, name='friend_list'),
    path('users/friend-request/send/<int:id>/', views.send_friend_request, name='send_friend_request'),
    path('users/friend-request/cancel/<int:id>/', views.cancel_friend_request, name='cancel_friend_request'),
    path('users/friend-request/accept/<int:id>/', views.accept_friend_request, name='accept_friend_request'),
    path('users/friend-request/delete/<int:id>/', views.delete_friend_request, name='delete_friend_request'),
    path('users/friend/delete/<int:id>/', views.delete_friend, name='delete_friend'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('my-profile/', views.my_profile, name='my_profile'),
    path('search_users/', views.search_users, name='search_users'),
    path('register/', views.register, name='register'),

    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),

    # feed
    path('', PostListView.as_view(), name='home'),

    path('post/new/', views.create_post, name='post-create'),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
    path('like/', views.like, name='post-like'),

    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),

    path('post/<int:pk>/delete/', views.post_delete, name='post-delete'),
    path('search_posts/', views.search_posts, name='search_posts'),
    
    path('user_posts/<str:username>', UserPostListView.as_view(), name='user-posts'),


    #chat
    path('chatapp/', views.chatapp, name='chat-chatapp'),

    path('send/', views.send_chat, name='chat-send'),
    path('renew/', views.get_messages, name='chat-renew'),
]
