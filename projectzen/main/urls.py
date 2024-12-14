from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('all_projects', views.all_projects, name='all_projects'),
     path('api/login/', views.login, name='login'),
    path('api/signup/', views.signup, name='signup'),
    path('api/test-token/', views.test_token, name='test_token'),
    path('login/', views.login_page, name='login_page'),
    path('signup/', views.signup_page, name='signup_page'),
    path('logout/', views.logout, name='logout'),
]
