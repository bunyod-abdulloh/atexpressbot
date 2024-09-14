from django.contrib import admin

from .models import Bemor


class BemorAdmin(admin.ModelAdmin):
    actions_on_top = False
    list_display = ('test_type', 'fullname',)
    list_display_links = ('fullname',)
    search_fields = ['fullname']


admin.site.register(Bemor, BemorAdmin)
