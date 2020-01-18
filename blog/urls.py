from django.urls import path
from .views import HomePageView, PostDetailView, AboutPageView, ContactPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    
]