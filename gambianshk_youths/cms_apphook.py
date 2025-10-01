from cms.app_base import CMSApp
from django.utils.translation import gettext_lazy as _
from cms.apphook_pool import apphook_pool

class GambianshkYouthsApphook(CMSApp):  
    app_name = "gambianshk_youths"
    name = _("Community App")
    urls = ["gambianshk_youths.urls"]
    menus = [
        "gambianshk_youths.menu.GambianshkMenu",
    ]

# Clear previous apphook registrations (optional, use carefully)
apphook_pool.clear()

# Register the apphook
apphook_pool.register(GambianshkYouthsApphook)  

print("Registering GambianshkYouthsApphook")
