from cms.menu_bases import CMSAttachMenu
from menus.base import NavigationNode
from menus.menu_pool import menu_pool
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class GambianshkMenu(CMSAttachMenu):
    name = _("Gambianshk Youths Menu")

    def get_nodes(self, request):
        nodes = []

        # Create NavigationNode instances for each item
        home_node = NavigationNode(
            title=_("Home"),
            url=reverse('gambianshk_youths:gambianshk_home'),
            id=1,
            parent_id=None,
        )

        members_node = NavigationNode(
            title=_("Members"),
            url=reverse('gambianshk_youths:member'),
            id=2,
            parent_id=None,
        )

        contributions_node = NavigationNode(
            title=_("Contributions"),
            url=reverse('gambianshk_youths:contribution_list'),
            id=3,
            parent_id=None,
        )

        projects_node = NavigationNode(
            title=_("Projects"),
            url=reverse('gambianshk_youths:projects_list'),
            id=4,
            parent_id=None,
        )

        events_node = NavigationNode(
            title=_("Events"),
            url=reverse('gambianshk_youths:events'),
            id=5,
            parent_id=None,
        )

        constitution_node = NavigationNode(
            title=_("Constitution"),
            url=reverse('gambianshk_youths:constitution'),
            id=6,
            parent_id=None,
        )

        community_node = NavigationNode(
            title=_("Community"),
            url=reverse('gambianshk_youths:community'),
            id=7,
            parent_id=None,
        )

        contacts_node = NavigationNode(
            title=_("Contact Us"),
            url=reverse('gambianshk_youths:contact_us'),  # Ensure this URL is defined
            id=8,
            parent_id=None,
        )

        # Append the NavigationNode instances to the list
        nodes.extend([
            home_node,
            members_node,
            contributions_node,
            projects_node,
            events_node,
            constitution_node,
            community_node,
            contacts_node,
        ])

        return nodes

menu_pool.register_menu(GambianshkMenu)
