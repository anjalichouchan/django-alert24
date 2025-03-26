from django.contrib import admin
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name = 'home'),
    path('india/',views.india, name= 'india'),
    path('bolly/',views.bolly, name= 'bollywood'),
    path('sports/',views.sports, name= 'sports'),
    path('health/',views.health, name= 'health'),
    path('details/<int:id>',views.details, name= 'details'),
    path('form/', views.studentView)
    ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
