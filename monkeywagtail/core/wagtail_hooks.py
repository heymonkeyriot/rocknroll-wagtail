from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register)
from .models import MainMenu


class MenuAdmin(ModelAdmin):
    model = MainMenu
    menu_label = 'Main menu'  # ditch this to use verbose_name_plural from model
    menu_icon = 'fa-bars'  # use font awesome if you want
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    # add_to_settings_menu = True  # or True to add your model to the Settings sub-menu
    list_display = ('title',)
    # https://docs.djangoproject.com/en/1.8/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display
    list_filter = ()
    search_fields = ('title',)

modeladmin_register(MenuAdmin)

# Note Andy Babic has now added exceptional documentation about ModelAdmin
# at http://docs.wagtail.io/en/latest/reference/contrib/modeladmin/index.html
