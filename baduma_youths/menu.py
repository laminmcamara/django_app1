# baduma_youths/menu.py
from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool
from django.utils.translation import gettext_lazy as _

class BadumaMenu(Menu):
    def get_nodes(self, request):
        return [
            NavigationNode(
                _("Members"), 
                "/members/", 
                "members",
                attr={'visible_for_anonymous': False}
            ),
            NavigationNode(
                _("Contributions"), 
                "/contributions/", 
                "contributions"
            )
        ]

menu_pool.register_menu(BadumaMenu)  # 👈 Critical registration line