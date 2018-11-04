from django.urls import path, include, re_path

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
]