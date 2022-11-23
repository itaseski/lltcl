from django.contrib import admin

from .models import Work

#@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ['code','title', 'short_description']
    list_display_links = ['code',]
    list_filter = ['status']
    search_fields = ['title', 'content']
    #prepopulated_fields = {"slug": ("title",)}
    # За да 'title' биде на кирилица а 'slug' на латиница, не може да се користи prepopolated_field.
    # raw_id_fields = ['author']

admin.site.register(Work, WorkAdmin)
