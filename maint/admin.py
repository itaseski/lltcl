from django.contrib import admin

from .models import Work

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ['code','title', 'content']
    list_display_links = ['code',]
    list_filter = ['status']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ['author']
