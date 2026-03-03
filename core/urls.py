from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('theme_pixel.urls')),
    # To jest kluczowa linia dla Twojej nowej aplikacji:
    path('', include('projects.urls')),
]