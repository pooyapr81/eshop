from django.urls import path
from . import views
app_name = 'accounts'
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('register/', views.register_view, name='register_view'),
    path('<user_id>/profile/', views.profile_view, name='profile'),
]
