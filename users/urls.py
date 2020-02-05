from django.urls import path

from users import views

urlpatterns = [
    path('home/', views.Home.as_view(), name='home'),
    # path('home/', views.Home.as_view(), name='home'),
]
