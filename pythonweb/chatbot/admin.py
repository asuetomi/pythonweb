from django.contrib import admin

# Register your models here.
from chatbot.models import Response, siritori, words

# admin.site.register(Response)
# admin.site.register(siritori)
# admin.site.register(words)


class ResponseAdmin(admin.ModelAdmin):
    list_display = ('keyword', 'text',)
    list_display_links = ('keyword', 'text',)


admin.site.register(Response, ResponseAdmin)


class SiritoriAdmin(admin.ModelAdmin):
    list_display = ('ruby', 'word', 'used',)
    list_display_links = ('ruby', 'word', 'used',)


admin.site.register(siritori, SiritoriAdmin)


class WordsAdmin(admin.ModelAdmin):
    list_display = ('word', 'mean',)
    list_display_links = ('word', 'mean',)


admin.site.register(words, WordsAdmin)
