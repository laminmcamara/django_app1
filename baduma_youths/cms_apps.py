from cms.app_base import CMSApp
from django.utils.translation import gettext_lazy as _

class BadumaYouthsApphook(CMSApp):
    app_name = "baduma_youths"
    name = _("Community App")
    urls = ["baduma_youths.urls"]
    menus = [
        "baduma_youths.menu.BadumaMenu",
    ]
