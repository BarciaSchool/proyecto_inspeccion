from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.user_login,name='login_page'),
    path('signup/',views.signup,name='signup_page')

]
