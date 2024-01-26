from django.contrib import admin
from django.urls import path
from home import views
# In your urls.py
from django.conf import settings
from django.conf.urls.static import static
from .views import register
    


urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("gallery", views.gallery, name='gallery'),
    path("contact", views.contact, name='contact'),
    path("login", views.login_user, name='login'),
    path("register", views.register, name='register'),
    path("logout", views.logout_user, name='logout'),
    path("home", views.home, name='home1'),
    path("futsal", views.futsal, name='futsal'),
    path("wedding", views.wedding, name='wedding'),
    path("music", views.music, name='music'),
    path("birthday", views.birthday, name='birthday'),
    path("final", views.final, name='final'),
    ] 


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)