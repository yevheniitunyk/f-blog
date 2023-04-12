from django.urls import include, path
from .views import *


urlpatterns = [
    path('', start_page, name='start_page'),
    path('login/', login_user, name='login_user'),
    path('sign-up/', signup_user, name='signup_user'),
    path('logout', logout_user, name='logout_user'),
    path('feed/category/<str:cattitle>', show_by_category, name='show_by_category'),
    path('feed/add_post/', add_post, name='add_post'),
    path('feed/post/<str:title>', show_detail, name='show_detail'),
]