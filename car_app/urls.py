from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login.as_view(), name='user_login'),
    # path('logout/', views.UserLogoutView.as_view(), name='user_logout'),
    path('logout/', views.user_logout, name='user_logout'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('pass_change/', views.pass_change.as_view(), name='pass_change'),
    path('details/<int:id>/', views.DetailCarView.as_view(), name='detail_car'),
]
