import os
from pathlib import Path
from dotenv import load_dotenv
from django.utils.translation import gettext_lazy as _
import secrets

from django.core.cache import cache


# Load environment variables from .env file
load_dotenv()

# BASE_DIR using pathlib for cleaner path handling
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY SETTINGS
# IMPORTANT: Replace the default SECRET_KEY in production with a secure, unique value.
# DEBUG = os.getenv('DJANGO_DEBUG', 'False').lower() in ['true', '1', 'yes']
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'fallback-secret-key')


# Get DEBUG status from an environment variable.
DEBUG = os.getenv('DJANGO_DEBUG', 'True').lower() in ['true', '1', 'yes']

# SECURITY SETTINGS - These are for production only.
if not DEBUG:
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True  # Enable HTTPS redirection in production
    # All other SECURE settings go here
else:
    # Optional: Set development-friendly values for security settings
    SECURE_SSL_REDIRECT = False
    CSRF_COOKIE_SECURE = False
    SESSION_COOKIE_SECURE = False

CMS_DEBUG = DEBUG


# SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', secrets.token_urlsafe(50))  # Use a secure key


# DEBUG should be False in production for security!
# import os


# Set your allowed hosts in production to your domain names or IPs.
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '127.0.0.1,localhost,thegambianshk.org,www.thegambianshk.org').split(',')

INSTALLED_APPS = [
    # Default Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'djangocms_text',
    'django_ckeditor_5', # The modern CKEditor 5 package

    # Third-party apps
    'corsheaders',
    'widget_tweaks',
    'parler',
    'cms',
    'menus',
    'treebeard',
    'sekizai',
    'easy_thumbnails',
    'filer',
    'djangocms_audio',
    'djangocms_file',
    'djangocms_picture',
    'djangocms_video',
    'djangocms_googlemap',
    'djangocms_snippet',
    'djangocms_style',
    'djangocms_versioning',
    'djangocms_alias', 

    # My apps
    # 'gambianshk_youths',
    'gambianshk_youths.apps.GambianshkYouthsConfig',
]


SITE_ID = 1
CMS_CONFIRM_VERSION4 = True

THUMBNAIL_HIGH_RESOLUTION = True

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)


# MIDDLEWARE
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Must be first to handle CORS properly
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # Locale middleware after sessions and common
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    # django CMS middleware
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',

    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# X_FRAME_OPTIONS = 'SAMEORIGIN'
X_FRAME_OPTIONS = 'DENY'


# DEPLOYMENT
# SECURE_HSTS_SECONDS = 31536000  # 1 year
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Optional
# SECURE_HSTS_PRELOAD = True  # Optional



# CMS Languages Configuration
CMS_LANGUAGES = {
    SITE_ID: [
        {'code': 'en', 'name': _('English'), 'public': True},
        {'code': 'ar', 'name': _('Arabic'), 'public': True},
        {'code': 'fr', 'name': _('French'), 'public': True},
    ],
}

# General Languages (for Django)
LANGUAGES = [
    ('en', _('English')),
    ('zh-hant', _('Traditional Chinese')),
    ('ar', _('Arabic')),
    ('fr', _('French')),
]

# django CMS Templates
CMS_TEMPLATES = [
    # The first template is the default for all new pages.
    ('gambianshk_youths/home.html', 'Homepage'),
    ('gambianshk_youths/community_detail_plugin.html', 'Community'),
    ('gambianshk_youths/constitution_detail_plugin.html', 'Constitution'),
    ('gambianshk_youths/event_list.html', 'Events'),
    ('gambianshk_youths/members.html', 'Our Members'),
    ('gambianshk_youths/project_detail_plugin.html', 'Our Projects'),
    ('gambianshk_youths/contact_us.html', 'Contact Us'),
    ('gambianshk_youths/privacy_policy.html', 'Privacy Policy'),
    ('gambianshk_youths/terms_conditions.html', 'Terms and Conditions'),
    ('gambianshk_youths/news.html', 'News'),
    ('gambianshk_youths/services.html', 'Our Services'),
  
]

# In your settings.py

CMS_PLACEHOLDER_CONF = {
    # This is the default list of plugins for any placeholder not specifically configured below.
    None: {
        "plugins": ["TextPlugin", "PicturePlugin", "LinkPlugin", "StylePlugin"],
        "excluded_plugins": [],
    },

    # Configuration for the "Members" page placeholders
    'page_title': {
        "plugins": ['TextPlugin'],
        'name': "Page Title and Intro",
    },
    'prominent_members': {
        "plugins": ['TextPlugin', 'PicturePlugin', 'StylePlugin'], # Add any custom "Card" plugin you might have
        'name': "Prominent Members Grid",
    },
    'honorary_members': {
        "plugins": ['TextPlugin', 'PicturePlugin', 'StylePlugin'],
        'name': "Honorary Members Grid",
    },
    'honorary_title': {
        "plugins": ['TextPlugin'],
        'name': "Honorary Section Title",
    },
    'in_memory_members': {
        "plugins": ['TextPlugin', 'PicturePlugin', 'StylePlugin'],
        'name': "In Memory Members Grid",
    },
    'join_call_to_action': {
        "plugins": ['TextPlugin', 'LinkPlugin'],
        'name': "Join Call to Action",
    },

    # Configuration for the new "Contact" page placeholders
    'contact_intro': {
        "plugins": ['TextPlugin'],
        'name': "Contact Page Introduction",
    },
    'contact_details': {
        "plugins": ['TextPlugin', 'LinkPlugin'],
        'name': "Contact Information (Address, Phone, Email)",
    },
    'contact_form': {
        # If you install a form plugin like 'djangocms-form-builder', add its name here.
        # For example: "plugins": ["FormBuilderPlugin"],
        'name': "Contact Form",
        'plugins': [], # Start with none until you install a form plugin
    },
    'contact_map': {
        "plugins": ['GoogleMapPlugin', 'TextPlugin'], # 'TextPlugin' allows adding an <iframe> directly
        'name': "Location Map",
    },
}

MENU_TEMPLATES = (
    ('menus/menu/default.html', 'Default menu template'),
)


# django CMS Apphooks
CMS_APPHOOKS = (
    'gambianshk_youths.cms_apphook.GambianshkYouthsApphook',
)



# URL Configuration
ROOT_URLCONF = 'gambianshk.urls'

# Templates Configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [    BASE_DIR / 'templates',
            BASE_DIR / 'gambianshk_youths' / 'templates'],  # Include app templates here
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # Required by django CMS
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'sekizai.context_processors.sekizai',  # For django CMS
                'cms.context_processors.cms_settings',  # For django CMS
            ],
        },
    },
]

# WSGI Application
WSGI_APPLICATION = 'gambianshk.wsgi.application'

# WSGI_APPLICATION = 'gambians_hk_web_project.wsgi.application'

# Database Configuration (default SQLite for development)
# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
# }
# TODO: For production, switch to a robust database like PostgreSQL.
# Example PostgreSQL config:
DATABASES = {
    'default': {
         'ENGINE': 'django.db.backends.postgresql',
         'NAME': os.getenv('POSTGRES_DB'),
         'USER': os.getenv('POSTGRES_USER'),
         'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
         'HOST': os.getenv('POSTGRES_HOST', 'localhost'),
         'PORT': os.getenv('POSTGRES_PORT', '5432'),
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
LOCALE_PATHS = [BASE_DIR / 'locale']

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# In development, serve static files from these directories
STATICFILES_DIRS = [BASE_DIR /'static']

# In production, collect static files here and serve via web server (e.g., Nginx)
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media files (User-uploaded content)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Path for CKEditor uploads
CKEDITOR_UPLOAD_PATH = "uploads/"




# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# CORS settings
# WARNING: Allow all origins only in development!
CORS_ALLOW_ALL_ORIGINS = DEBUG

# Cache settings - simple in-memory cache for development
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_ALLOW_NONIMAGE_FILES = True  # Allow other uploads
CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': [
            ['Undo', 'Redo'],
            ['CMSplugins', '-', 'ShowBlocks'],
            ['Format', 'Styles'],
            ['TextColor', 'BGColor', '-', 'PasteText', 'PasteFromWord'],
            ['Maximize', ''],
            '/',
            ['Bold', 'Italic', 'Underline', '-', 'Subscript', 'Superscript', '-', 'RemoveFormat'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight'],
            ['HorizontalRule', 'Link', 'Unlink'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Table'],
            ['ImageUpload', 'MediaEmbed', 'insertImage'],  # Include ImageUpload and MediaEmbed
            ['Source']
        ],
        'language': '{{ language }}',  # Dynamically set in templates or views
        'filebrowserUploadUrl': '/upload/media/',  # URL for media uploads
        'mediaEmbed': {
            'providers': [
                {
                    'name': 'youtube',
                    'url': r'^https?://(www\.)?youtube\.com/watch\?v=([a-zA-Z0-9_-]{11})$',
                    'html': r'<iframe width="560" height="315" src="https://www.youtube.com/embed/$2" frameborder="0" allowfullscreen></iframe>'
                },
                {
                    'name': 'vimeo',
                    'url': r'^https?://(www\.)?vimeo\.com/([0-9]+)$',
                    'html': r'<iframe src="https://player.vimeo.com/video/$2" width="640" height="360" frameborder="0" allowfullscreen></iframe>'
                },
                # Add more providers if needed
            ]
        },
        'image': {
            'toolbar': [
                'imageTextAlternative', '|', 
                'imageStyle:alignLeft', 'imageStyle:alignRight', 
                'imageStyle:alignCenter', 'imageStyle:side', '|'
            ],
            'styles': [
                'full', 'side', 'alignLeft', 'alignRight', 'alignCenter',
            ]
        },
        'extraPlugins': ['uploadimage', 'mediaembed'],  # Ensure these plugins are included
    },
    'text': {
        'toolbar': ['bold', 'italic', 'link'],
    },
    'my-custom-toolbar': {
        'toolbar': [
            'heading', '|', 'outdent', 'indent', '|', 'bold', 
            'italic', 'link', 'underline', 'strikethrough', 'code',
            'subscript', 'superscript', 'highlight', '|', 'codeBlock', 
            'sourceEditing', 'insertImage', 'bulletedList', 
            'numberedList', 'todoList', '|', 'blockQuote', 
            'imageUpload', 'MediaEmbed', '|', 'fontSize', 
            'fontFamily', 'fontColor', 'fontBackgroundColor', 
            'mediaEmbed', 'removeFormat', 'insertTable',
        ],
    }
}


# Additional deployment tips:
# - Use a production-ready web server like Gunicorn or uWSGI behind Nginx or Apache.
# - Set up HTTPS with certificates (Let's Encrypt recommended).
# - Use environment variables for all secrets and sensitive configs.
# - Run `python manage.py collectstatic` during deployment.
# - Configure proper logging for production.
# - Regularly update dependencies and Django for security patches.
