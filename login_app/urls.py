from django.urls import path
from . import views
app_name ='login_app'

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('', views.log_in, name='login'),
    path('edit_profile/', views.Edit_profile, name='edit_profile'),
    path('user_logout/', views.logout_user, name='log_out'),
    path('user/', views.user, name='user'),
]
