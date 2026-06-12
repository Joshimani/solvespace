from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user/sign_up', views.sign_up, name='sign_up'),
    path('user/login', views.login, name='login'),
    path('user/details', views.user_details, name='user_details'),
    path('user/update', views.update_user_details, name='update_user_details'),
    path('user/logout', views.logout, name='logout'),
    path('user/delete', views.delete_user, name='delete_user')

]