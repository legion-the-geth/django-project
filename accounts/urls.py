from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    # ex: /accounts/widget/
    path('widget/', views.widget, name='widget'),
    # ex: /accounts/login/
    path('login/', views.login, name='login'),
    # ex: /accounts/logout/
    path('logout/', views.logout, name='logout'),
]
