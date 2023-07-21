from django.urls import path
from authenticate import views

app_name = 'authenticate'

urlpatterns = [
    path('admin-login/', views.login_view, name='login_admin')
]
