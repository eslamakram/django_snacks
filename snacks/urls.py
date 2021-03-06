from django.urls import path
from django.urls.resolvers import URLPattern
from .views import HomeView, AboutUsView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about-us/', AboutUsView.as_view(), name= 'about_us'),
]