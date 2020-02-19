from django.urls import path

from blog.views import python_views


urlpatterns = [
    # Python
    path('python/', python_views.Pyhome.as_view(), name='python/home'),
]