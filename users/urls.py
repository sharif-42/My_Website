from django.urls import path

from users import views

urlpatterns = [
    path('dashboard/', views.Home.as_view(), name='home'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('password_change/', views.ChangePassword.as_view(), name='password_change'),

]
