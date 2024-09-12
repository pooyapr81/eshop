from django.urls import path
from . import views
app_name = 'accounts'
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login_view'),
]
