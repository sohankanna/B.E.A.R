from django.urls import path
from . import views
from .views import login_view, dashboard_view, logout_view
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
     path('login/', login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('pricing/',views.pricing, name='pricing'),
    path('signupsuccess/',views.signupsuccess, name="signupsuccess"),
    path('dashboard/', dashboard_view, name='dashboard'),  # Dynamic URL for dashboard
    path('logout/', logout_view, name='logout'),
]