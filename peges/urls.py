from .views import homePageView,HomePageView ,AboutPageView
from django.urls import path


urlpatterns = [
    path('', homePageView, name='home'),
    path('homepage/',HomePageView.as_view(), name='home_page'),
    path('aboutpage/',AboutPageView.as_view(), name='about_page'),
]
