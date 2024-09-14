from django.contrib import admin

from .models import Table1, Table2, Table3, Table4, Table5, Table6, Table7, Table8


class CommonAdmin(admin.ModelAdmin):
    actions_on_top = False
    list_display = ('lesson_number', 'file_name', 'caption')
    list_display_links = ('lesson_number',)
    ordering = ('lesson_number',)


tables = [Table1, Table2, Table3, Table4, Table5, Table6, Table7, Table8]

for table in tables:
    admin.site.register(table, CommonAdmin)
