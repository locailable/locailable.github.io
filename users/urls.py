from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),  # Fix the line here
    path('user-profile/<uuid:owner_id>/', views.userProfile, name='user_profile'),
    path('account/', views.userAccount, name='account'),
    path('edit-account/', views.editAccount, name='edit_account'),
]
