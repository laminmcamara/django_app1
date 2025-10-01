# baduma_project/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 1. The admin interface must come first so it is always found.
    path('admin/', admin.site.urls),
    
    # Include URLs from the gambianshk_youths app with namespace
    path('gambianshk_youths/', include(('gambianshk_youths.urls', 'gambianshk_youths'), namespace='gambianshk_youths')),
    
    # 2. Django CMS must come last. It acts as the "catch-all" for your
    #    homepage and any other page you create in the CMS.
    path('', include('cms.urls')),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    # path('ckeditor/', include('ckeditor_uploader.urls')), 
]

# This is standard best practice for serving images and other files
# during development.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)