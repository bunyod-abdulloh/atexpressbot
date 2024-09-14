from django.contrib import admin

from .models import Table9, Table10, Tables


class TablesAdmin(admin.ModelAdmin):
    actions_on_top = False
    list_display = ('table_number', 'table_name', 'table_type',)
    list_display_links = ('table_name',)
    ordering = ('table_number',)


class Table9Admin(admin.ModelAdmin):
    actions_on_top = False
    list_display = ('sequence', 'subcategory', 'category',)
    list_display_links = ('subcategory',)
    ordering = ('sequence',)
    list_filter = ('category',)


class Table10Admin(admin.ModelAdmin):
    list_display = ('id', 'file_name',)
    list_display_links = ('file_name',)
    ordering = ('id',)


admin.site.register(Table9, Table9Admin)
admin.site.register(Table10, Table10Admin)
admin.site.register(Tables, TablesAdmin)
