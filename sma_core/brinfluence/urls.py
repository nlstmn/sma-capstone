from django.urls import path,include,re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    path('influencer/<username>/', views.influencer_profile, name='influencer_profile' ),
    path('brand/<username>/', views.brand_profile, name='brand_profile'),
    path('influencer/<username>/recommended/', views.influencer_recommended, name="influencer_recommender"),
    path('brand/<username>/recommended/', views.brand_recommended, name='brand_recommended')
]