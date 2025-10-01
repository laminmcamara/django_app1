from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _
import logging

logger = logging.getLogger(__name__)

class GambianshkYouthsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gambianshk_youths'  # Ensure this matches app name
    verbose_name = _("Community Management")

    def ready(self):
        # Register CMS app hooks
        try:
            from .cms_apphook import GambianshkYouthsApphook  # Ensure this file exists and is correctly named
            from cms.apphook_pool import apphook_pool

            # Check if the apphook is already registered
            if GambianshkYouthsApphook not in apphook_pool.get_apphooks():  
                apphook_pool.register(GambianshkYouthsApphook)
                logger.info("GambianshkYouthsApphook registered successfully.")
            else:
                logger.debug("GambianshkYouthsApphook already registered.")
        except ImportError as e:
            logger.error(f"Failed to import GambianshkYouthsApphook: {e}")
        except Exception as e:
            logger.error(f"Unexpected error during apphook registration: {e}")
