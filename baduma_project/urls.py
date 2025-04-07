from django.contrib import admin
from django.urls import include, path
from baduma_youths.views import home, custom_404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cms.urls')),
    #path('', home, name='pages-root'),  # Home route defined here
    path('', include('baduma_youths.urls',  namespace='baduma_youths')),  # Include app-level URLs
]

# Custom error handlers
handler404 = custom_404
