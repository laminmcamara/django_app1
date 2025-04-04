from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class BadumaYouthsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'baduma_youths'
    verbose_name = _("Community Management")

    def ready(self):
        # Register CMS app hooks
        try:
            from .cms_apps import BadumaYouthsApphook
            from cms.apphook_pool import apphook_pool

            # Check if the apphook is already registered
            if BadumaYouthsApphook.__name__ not in apphook_pool.apphooks:
                apphook_pool.register(BadumaYouthsApphook)
        except ImportError:
            pass
