from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

urlpatterns = [
    path('test/', views.test_chat, name='test_chat'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', views.chat_dashboard, name='chat_dashboard'),
    path('add_friend/', views.add_friend, name='add_friend'),
    path('start/<int:friend_id>/', views.start_chat, name='start_chat'),
    path('<int:conversation_id>/', views.conversation_chat, name='conversation_chat'),
]
