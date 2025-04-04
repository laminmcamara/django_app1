from django.contrib import admin
from django.urls import path, include
from baduma_youths.views import home, custom_404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Home route defined here
    path('', include('baduma_youths.urls')),  # Include app-level URLs
]

# Custom error handlers
handler404 = custom_404
