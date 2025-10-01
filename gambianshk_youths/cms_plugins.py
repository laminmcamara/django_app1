from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _
from .models import  Constitution, Member, Contribution, Expense, Budget, FinancialReport, Event, Meeting, ImageFlexbox, Project

# Define the ConstitutionPlugin
class ConstitutionPlugin(CMSPluginBase):
    model = Constitution  # Use the Constitution model
    name = _("Constitution")
    render_template = "gambianshk_youths/constitution_detail_plugin.html"  # Update with your template path
    text_enabled = True

plugin_pool.register_plugin(ConstitutionPlugin)

# Define the MemberPlugin
class MemberPlugin(CMSPluginBase):
    model = Member  # Use the Member model
    name = _("Member")
    render_template = "gambianshk_youths/member_detail_plugin.html"  # Update with your template path
    text_enabled = True

plugin_pool.register_plugin(MemberPlugin)

# Define the ContributionPlugin
class ContributionPlugin(CMSPluginBase):
    model = Contribution  # Use the Contribution model
    name = _("Contribution")
    render_template = "gambianshk_youths/contribution_detail_plugin.html"  # Update with your template path
    text_enabled = True

plugin_pool.register_plugin(ContributionPlugin)

# Define the ExpensePlugin
class ExpensePlugin(CMSPluginBase):
    model = Expense  # Use the Expense model
    name = _("Expense")
    render_template = "gambianshk_youths/expense_detail_plugin.html"  # Update with your template path
    text_enabled = True

plugin_pool.register_plugin(ExpensePlugin)

# Define the BudgetPlugin
class BudgetPlugin(CMSPluginBase):
    model = Budget  # Use the Budget model
    name = _("Budget")
    render_template = "gambianshk_youths/budget_detail_plugin.html" 
    text_enabled = True

plugin_pool.register_plugin(BudgetPlugin)

# Define the FinancialReportPlugin
class FinancialReportPlugin(CMSPluginBase):
    model = FinancialReport  # Use the FinancialReport model
    name = _("Financial Report")
    render_template = "gambianshk_youths/financial_report_detail_plugin.html"  
    text_enabled = True

plugin_pool.register_plugin(FinancialReportPlugin)

# Define the EventDetailPlugin
class EventDetailPlugin(CMSPluginBase):
    model = Event  # Use the Event model
    name = _("Event")
    render_template = "gambianshk_youths/event_detail_plugin.html"  # Update with your template path
    text_enabled = True

plugin_pool.register_plugin(EventDetailPlugin)

# Define the MeetingPlugin
class MeetingPlugin(CMSPluginBase):
    model = Meeting  # Use the Meeting model
    name = _("Meeting")
    render_template = "gambianshk_youths/meeting_detail.html"  
    text_enabled = True

plugin_pool.register_plugin(MeetingPlugin)

# Define the ImageFlexboxPlugin
class ImageFlexboxPlugin(CMSPluginBase):
    model = ImageFlexbox  # Use the ImageFlexbox model
    name = _("Image Flexbox")
    render_template = "gambianshk_youths/image_flexbox.html"  

plugin_pool.register_plugin(ImageFlexboxPlugin)
