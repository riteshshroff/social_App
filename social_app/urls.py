from django.contrib import admin
from django.urls import path, include
from social_app import views


urlpatterns = [
    path('', views.home),
    path('social-home/', views.social_home, name='social-home'),
    path('user-signup/', views.user_signup, name='user-signup'),
    path('save-users/', views.save_users, name='save-users'),
    path('save-post/', views.save_post, name='save-post'),
    path('logout/', views.logout, name="logout"),
    path('users-profile/', views.users_profile, name='users-profile'),
    path('update-user-profile/', views.update_user_profile, name='update-user-profile'),
    path('add-friend/', views.add_friend, name='add-friend'),
    path('user-connections/', views.user_connections, name='user-connections'),  
    path('mutual-connections/',views.mutual_connections, name='mutual-connections'),
    path('view-connection-details/', views.view_connection_details, name='view-connection-details'),
    path('view-mutual-connections-details/', views.view_mutual_connections_details, name='view-mutual-connections-details'),
    path('search-connections/', views.search_connections, name="search-connections"),
]

