from django.contrib.auth import views as auth_views
from django.urls import include, path
from .views import CreateUser, UpdateUserInfo, ChangePassword, AuthorInfo, UpdateUserProfile, CreateUserProfile


urlpatterns = [
    path('login/',auth_views.LoginView.as_view(),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('register/',CreateUser.as_view(),name='register'),
    path('update_profile/',UpdateUserInfo.as_view(),name='update_profile'),
    path('password/', ChangePassword.as_view(),name='change_password'),
    path('author_info/<int:pk>/',AuthorInfo.as_view(),name='author_info'),
    path('update_user_profile/<int:pk>/',UpdateUserProfile.as_view(),name='update_user_profile'),
    path('create_user_profile',CreateUserProfile.as_view(),name='create_user_profile'),
]