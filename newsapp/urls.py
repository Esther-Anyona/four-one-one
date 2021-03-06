from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name="profile"),
    path('profile/<str:username>/edit', views.edit_profile, name="edit_profile"),
    path('search', views.search, name="search"),

]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT)