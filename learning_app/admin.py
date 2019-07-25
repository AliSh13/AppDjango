from django.contrib import admin
from learning_app.models import Topic, Entry

class EntryAdmin(admin.ModelAdmin):
    list_display = ('name_topic', 'text', 'date_add')
    list_display_links = ('text', )
    search_fields = ('text', )


admin.site.register(Topic)
admin.site.register(Entry, EntryAdmin)
